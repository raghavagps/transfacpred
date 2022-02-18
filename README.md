# **TransFacPred**
A highly accurate method to predict the transcription factors using protein sequences.
## Introduction
TransFacPred is developed for predicting the transcription factors (TFs) using the protein primary sequence information. In this approach, two deep-learning based models have been implemented, such as ProtBert and Hybrid model which is a combination of CNN and BLAST Search.
TransFacPred is also available as web-server at https://webs.iiitd.edu.in/raghava/transfacpred. Please read/cite the content about the TransFacPred for complete information including algorithm behind TransFacPred.

## Standalone
The Standalone version of transfacpred is written in python3 and following libraries are necessary for the successful run:
- scikit-learn
- Keras
- Pytorch
- Pandas
- Numpy
### Important Note
- Due to large size of the model and database files, we have not included them in the zipped folder or GitHub repository, hence to run standalone successfully you need to download two file and then have to unzip them.
- Make sure you extract the download zip files in the directory where main execution file i.e. transfacpred.py is available.
- To download the Database folder click [here].(https://webs.iiitd.edu.in/raghava/transfacpred/database.zip)
- To download the Model folder click [here].(https://webs.iiitd.edu.in/raghava/transfacpred/Models.zip)

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
                       [-m {1,2}]
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
                        Threshold: Value between 0 to 1 by default 0.1
  -m {1,2}, --model {1,2}
                        Model: 1: ProtBert based approach, 2: Hybrid (CNN+BLAST) approach, by default 1
  -d {1,2}, --display {1,2}
                        Display: 1:Transcription Factors, 2: All Sequences, by default 1
```

**Input File:** It allow users to provide input in the FASTA format.

**Output File:** Program will save the results in the CSV format, in case user do not provide output file name, it will be stored in "outfile.csv".

**Threshold:** User should provide threshold between 0 and 1.
