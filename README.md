# **TransFacPred**
A highly accurate method to predict the transcription factors using protein sequences.
## Introduction
TransFacPred is developed for predicting the transcription factors (TFs) using the protein primary sequence information. In this approach, two deep-learning based models have been implemented, such as ProtBert and Hybrid model which is a combination of CNN and BLAST Search.
TransFacPred is also available as web-server at https://webs.iiitd.edu.in/raghava/transfacpred. Please read/cite the content about the TransFacPred for complete information including algorithm behind TransFacPred.

Models: In this program, two models have been incorporated for predicting TFs. 1) ProtBert Based Model 2) Hybrid (CNN+BLAST) model

Minimum USAGE: Minimum usage is "python transfacpred.py -i protein.fa," where protein.fa is a input fasta file. This will predict if the submitted sequences are TFs or Non-TFs. It will use other parameters by default. It will save output in "outfile.csv" in CSV (comma seperated variables).

Full Usage: Following is complete list of all options, you may get these options by "python transfacpred.py -h" 

usage: transfacpred.py [-h] -i INPUT [-o OUTPUT] [-t THRESHOLD] [-m {1,2}] [-d {1,2}]

Please provide following arguments

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input: File name containing protein or peptide sequence in FASTA format.
  -o OUTPUT, --output OUTPUT
                        Output: File for saving results by default outfile.csv
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold: Value between 0 to 1 by default 0.1
  -m {1,2}, --model {1,2}
                        Model: 1: ProtBert based approach, 2: Hybrid (CNN+BLAST) approach, by default 1
  -d {1,2}, --display {1,2}
                        Display: 1:Transcription Factors, 2: All Sequences, by default 1

**Input File:** It allow users to provide input in two format; i) FASTA format (standard) and ii) Simple Format. In case of simple format, file should have one peptide sequence in a single line in single letter code. 

**Output File:** Program will save the results in the CSV format, in case user do not provide output file name, it will be stored in "outfile.csv".

**Threshold:** User should provide threshold between 0 and 1.


TransFacPred Package Files
=======================
It contantain following files, brief descript of these files given below

INSTALLATION  			: Installations instructions

LICENSE       			: License information

README.md     			: This file provide information about this package

Models        		        : This folder comprises of models needed for the prediction

transfacpred.py 		: Main python program 

protein.fa			: Example file contain protein sequenaces in FASTA format 

example_output_protbert.csv	: Example output file using model 1, i.e. ProtBert Model

example_output_hybrid.csv	: Example output file using model 2. i.e. Hybrid Model (CNN+BLAST)

envfile				: This file comprises of the path for BLASTP and database
