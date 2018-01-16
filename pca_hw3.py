# -*- coding: utf-8 -*-
# Code is writtern in python 2
# Implementation of PCA
# code written by
# Radhika Agarwal


import numpy as np
import pandas as pd
import sys
#location=r"C:\Users\amiya\Desktop\USC GRAD\Machine Learning\Assignment\HW3\pca-data.txt"

location = sys.argv[1]
data=pd.read_table(location)
table=pd.DataFrame.as_matrix(data)

#calculating covariance manually
mean_val=np.mean(table,axis=0)
sub=table-mean_val
covariance_matrix = (sub).T.dot((sub)) / (len(sub)-1)

#Eigen vectors and Eigen values
e_vals,e_vects=np.linalg.eig(covariance_matrix)

#Finding Eigen vectors based on Max eigen values:
val=(-e_vals).argsort()[:2]
result=e_vects[...,val]
print result.T

# data modified into a lower dimension
reduced=np.dot(table,result)
#print "modified data set\n",reduced
