##############################################################################
# TransFacPred is developed for predicting Transcription Factors using protein #
# Sequence information. It is developed by Prof G. P. S. Raghava's group.      #
# Please Cite: https://webs.iiitd.edu.in/raghava/transfacpred/                 #
# ############################################################################
import argparse  
import warnings
import pickle
import os
import re
import uuid
import sys
import numpy as np
import pandas as pd
import pickle
import zipfile
from sklearn.ensemble import ExtraTreesClassifier
warnings.filterwarnings('ignore')
parser = argparse.ArgumentParser(description='Please provide following arguments') 

## Read Arguments from command
parser.add_argument("-i", "--input", type=str, required=True, help="Input: File name containing protein or peptide sequence in FASTA format.")
parser.add_argument("-o", "--output",type=str, help="Output: File for saving results by default outfile.csv")
parser.add_argument("-t","--threshold", type=float, help="Threshold: Value between 0 to 1 by default -0.38")
parser.add_argument("-d","--display", type=int, choices = [1,2], help="Display: 1:Transcription Factors, 2: All Sequences, by default 1")
args = parser.parse_args()

def readseq(file):
    with open(file) as f:
        records = f.read()
    records = records.split('>')[1:]
    seqid = []
    seq = []
    for fasta in records:
        array = fasta.split('\n')
        name, sequence = array[0].split()[0], re.sub('[^ACDEFGHIKLMNPQRSTVWY-]', '', ''.join(array[1:]).upper())
        seqid.append('>'+name)
        seq.append(sequence)
    if len(seqid) == 0:
        f=open(file,"r")
        data1 = f.readlines()
        for each in data1:
            seq.append(each.replace('\n',''))
        for i in range (1,len(seq)+1):
            seqid.append(">Seq_"+str(i))
    df1 = pd.DataFrame(seqid)
    df2 = pd.DataFrame(seq)
    return df1,df2

def aac_comp(file):
    std = list('ACDEFGHIKLMNPQRSTVWY')
    df1 = file
    df1.columns = ['Seq']
    dd = []
    for j in df1['Seq']:
        cc = []
        for i in std:
            count = 0
            for k in j:
                temp1 = k
                if temp1 == i:
                    count += 1
                composition = (count/len(j))*100
            cc.append(composition)
        dd.append(cc)
    df2 = pd.DataFrame(dd)
    head = []
    for mm in std:
        head.append('AAC_'+mm)
    df2.columns = head
    return df2

def pred(file1,file2):
    a = []
    clf = pickle.load(open(file2,'rb'))
    data_test = file1
    y_p_score1=clf.predict_proba(data_test)
    y_p_s1=y_p_score1.tolist()
    a.extend(y_p_s1)
    df_a = pd.DataFrame(a)
    df_1a = df_a.iloc[:,-1].round(2)
    df_2a = pd.DataFrame(df_1a)
    df_2a.columns = ['ML_score']
    return df_2a

def BLAST_processor(blast_result,name1,ml_results,thresh):
    if os.stat(blast_result).st_size != 0:
        df1 = pd.read_csv(blast_result, sep="\t", names=['name','hit','identity','r1','r2','r3','r4','r5','r6','r7','r8','r9'])
        df2 = name1
        df3 = ml_results
        cc = []
        for i in df2[0]:
            kk = i.replace('>','')
            if len(df1.loc[df1.name==kk])>0:
                df4 = df1[['name','hit']].loc[df1['name']==kk].reset_index(drop=True)
                if df4['hit'][0].split('_')[0]=='P':
                    cc.append(0.5)
                if df4['hit'][0].split('_')[0]=='N':
                    cc.append(-0.5)
            else:
                cc.append(0)
        df6 = pd.DataFrame()
        df6['Seq_ID'] = [i.replace('>','') for i in df2[0]] 
        df6['ML_Score'] = df3['ML_score']
        df6['BLAST_Score'] = cc
        df6['Total_Score'] = df6['ML_Score']+df6['BLAST_Score']
        df6['Prediction'] = ['Transcription Factor' if df6['Total_Score'][i]>thresh else 'Non-Transcription Factor' for i in range(0,len(df6))]
    else:
        df2 = name1
        ss = []
        vv = []
        for j in df2[0]:
            ss.append(j.replace('>',''))
            vv.append(0)
        df6 = pd.DataFrame()
        df6['Seq_ID'] = ss
        df6['ML_Score'] = df3['ML_score']
        df6['BLAST_Score'] = vv
        df6['Total_Score'] = df6['ML_Score']+df6['BLAST_Score']
        df6['Prediction'] = ['Transcription Factor' if df6['Total_Score'][i]>thresh else 'Non-Transcription Factor' for i in range(0,len(df6))]
    return df6

print('##############################################################################')
print('# This program TransFacPred is developed for predicting Transcription   #')
print('# factors, developed by Prof G. P. S. Raghava\'s group.                    #')
print('# ############################################################################')

# Parameter initialization or assigning variable for command level arguments

Sequence= args.input        # Input variable 
 
# Output file 
 
if args.output == None:
    result_filename= "outfile.csv" 
else:
    result_filename = args.output
         
# Threshold 
if args.threshold == None:
        Threshold = -0.38
else:
        Threshold= float(args.threshold)
# Display
if args.display == None:
        dplay = int(1)
else:
        dplay = int(args.display)

print('Summary of Parameters:')
print('Input File: ',Sequence,'; Threshold: ', Threshold)
print('Output File: ',result_filename,'; Display: ',dplay)

#======================= Prediction Module start from here =====================
print("======Initiating Prediction Using Hybrid Model. Please Wait.......================")
if os.path.exists('envfile'):
    with open('envfile', 'r') as file:
        data = file.readlines()
    output = []
    for line in data:
        if not "#" in line:
            output.append(line)
    if len(output)==2: 
        paths = []
        for i in range (0,len(output)):
            paths.append(output[i].split(':')[1].replace('\n',''))
        blastp = paths[0]
        blastdb = paths[1]
    else:
        print("####################################################################################")
        print("Error: Please provide paths for BLAST, and required files", file=sys.stderr)
        print("####################################################################################")
        sys.exit()
 
else:
    print("####################################################################################")
    print("Error: Please provide the '{}', which comprises paths for BLAST".format('envfile'), file=sys.stderr)
    print("####################################################################################")
    sys.exit()

filepath = os.path.dirname(os.path.abspath(__file__))
if os.path.isdir('Models') == False:
    with zipfile.ZipFile(filepath+'/Models.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
else:
    pass
if os.path.isdir('database') == False:
    with zipfile.ZipFile(filepath+'/database.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
else:
    pass
df_2b,df_1b = readseq(Sequence)
df_3b = aac_comp(df_1b)
df_4b = pred(df_3b,filepath+'/Models/ET_model.pkl')
os.system(blastp + " -task blastp -db " + blastdb + " -query " + Sequence  + " -out RES_1_6_6.out -outfmt 6 -evalue 100")
df44 = BLAST_processor('RES_1_6_6.out',df_2b,df_4b,Threshold)
if dplay == 1:
    df44 = df44.loc[df44.Prediction=="Transcription Factor"]
else:
    df44 = df44
df44 = round(df44,3)
df44.to_csv(result_filename, index=None)
os.remove('RES_1_6_6.out')
print("\n=========Process Completed. Have an awesome day ahead.=============\n")
print('\n======= Thanks for using TransFacPred. Your results are stored in file :',result_filename,' =====\n\n')
