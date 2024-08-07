# **TransFacPred**
A highly accurate method to predict the transcription factors using protein sequences.
## Introduction
TransFacPred is developed for predicting the transcription factors (TFs) using the protein primary sequence information. In this approach, Hybrid model was implemented in which is a combination of ET-based model and BLAST Search.
TransFacPred is also available as web-server at https://webs.iiitd.edu.in/raghava/transfacpred. Please read/cite the content about the TransFacPred for complete information including algorithm behind TransFacPred.

## PIP Installation
PIP version is also available for easy installation and usage of this tool. The following command is required to install the package 
```
pip install transfacpred
```
To know about the available option for the pip package, type the following command:
```
transfacpred -h
```
## Standalone
The Standalone version of transfacpred is written in python3 and following libraries are necessary for the successful run:
- scikit-learn
- Pandas
- Numpy

**Important: NCBI-BLAST version [2.2.29+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.29/) is strongly recommended for optimal compatibility with the hybrid model, as it was developed using this specific version. Utilizing a different version may lead to inconsistencies between the outputs obtained from the web server and the standalone application.**
### Important Note
- Due to large size of the model and database files, we have not included them in the zipped folder or GitHub repository, hence to run standalone successfully you need to download two file and then have to unzip them.
- Make sure you extract the download zip files in the directory where main execution file i.e. transfacpred.py is available.
- To download the Database folder (120 MB) click [here](https://webs.iiitd.edu.in/raghava/transfacpred/database.zip).
- To download the Model folder (135 MB) click [here](https://webs.iiitd.edu.in/raghava/transfacpred/Models.zip).

## Minimum USAGE
To know about the available option for the stanadlone, type the following command:
```
python transfacpred.py -h
```
To run the example, type the following command:
```
python3 transfacpred.py -i protein.fa
```
This will predict if the submitted sequences are TFs or Non-TFs. It will use other parameters by default. It will save the output in "outfile.csv" in CSV (comma seperated variables).

## Full Usage
```
usage: transfacpred.py [-h] 
                       [-i INPUT 
                       [-o OUTPUT]
                       [-t THRESHOLD]
                       [-d {1,2}]
```
```
Please provide following arguments for successful run

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input: File name containing protein or peptide sequence in FASTA format.
  -o OUTPUT, --output OUTPUT
                        Output: File for saving results by default outfile.csv
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold: Value between -0.5 to 1.5 by default -0.38
  -d {1,2}, --display {1,2}
                        Display: 1:Transcription Factors, 2: All Sequences, by default 1
```

**Input File:** It allow users to provide input in the FASTA format.

**Output File:** Program will save the results in the CSV format, in case user do not provide output file name, it will be stored in "outfile.csv".

**Threshold:** User should provide threshold between -0.5 and 1.5.
# Reference
Patiyal S, Tiwari P, Ghai M, Dhapola A, Dhall A and Raghava GPS (2024) A hybrid approach for predicting transcription factors. <a href="https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2024.1425419">Front. Bioinform. 4:1425419.
 </a> 
