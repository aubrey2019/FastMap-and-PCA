# -*- coding: utf-8 -*-
# Code is writtern in python 2
# Implementation of PCA
# code written by:
# Aayush Sinha
# Abhishek Jangalwa
# Radhika Agarwal


import pandas as pd
import sys
from sklearn.decomposition import PCA
#location=r"C:\Users\amiya\Desktop\USC GRAD\Machine Learning\Assignment\HW3\pca-data.txt"
location = sys.argv[1]
data=pd.read_table(location)
table=pd.DataFrame.as_matrix(data)

result= PCA(n_components=2)
result.fit_transform(table)

output=result.components_
print output