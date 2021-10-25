"""
This is an implementation of the naive Bayes Model based on https://www.kaggle.com/prashant111/naive-bayes-classifier-in-python
The Dataset used here is the adult dataset from https://archive.ics.uci.edu/ml/datasets/Adult in csv 

"""

#Different libraries needed are imported

import pandas as pd  
import category_encoders as ce
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from sklearn.model_selection import train_test_split as tst
from sklearn.preprocessing import RobustScaler as rs
from sklearn.naive_bayes import GaussianNB as gnb
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings("ignore")



#Getting the path of a the dataset
directory=os.getcwd()
for path, directories, files in os.walk(directory):
    for file in files:
        print(file)
data_directory=directory+"\\adult.csv"
print(data_directory)

#Reading the data
df=pd.read_csv(data_directory, header=None, sep=".\s")

#Getting informations on the data

df.shape #number of rows and columns
df.head() #first five rows of the data


""" Data Preprocessing """
#Naming all different columns accordingly
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship','race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
df.columns=col_names
df.head()
df.info() # Informations about the dataset