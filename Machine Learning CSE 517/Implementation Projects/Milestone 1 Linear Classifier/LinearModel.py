# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 1
Linear Model
wisconsin breast cancer database used 

@author: KMShihab
"""

import numpy as np
from utilityFunctions import *

#Constant parameters
NO_OF_FEATURES=30
NO_OF_SAMPLES=569
CROSS_VALIDATION_K=10

#######################################
#X(i) is feature vector, Y(i) is label for i-the sample
########################################
X=np.ones((NO_OF_SAMPLES,NO_OF_FEATURES+1))
Y=np.zeros((NO_OF_SAMPLES,1))
W=np.zeros((NO_OF_FEATURES,1))

#print(label)
##########################################
# Reading file and formatting data
##########################################
fileInput = open('wdbc.data', 'r')
indexSample=0
for line in fileInput:
    data=line.split(',')
    features=list(map(float,data[2:]))
    # 1 for malignant tumor, -1 for benign tumor
    label=1 if data[1]=='M' else -1
    
    X[indexSample,1:]=features
    Y[indexSample]=label
    indexSample+=1
       
fileInput.close()

####################################
#Training & Testing
###################################
accuracyMeasures=np.array([0, 0, 0, 0]);#TP,TN,FP,FN
for n_k in CROSS_VALIDATION_K:
    ss

