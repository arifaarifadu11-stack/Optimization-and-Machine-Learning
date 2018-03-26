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
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, RationalQuadratic, ExpSineSquared
#Constant parameters
NO_OF_FEATURES=30
NO_OF_SAMPLES=569
CROSS_VALIDATION_K=10

#######################################
#for i-th sample
#X(i) is feature vector, Y(i) is label 
########################################
X=np.ones((NO_OF_SAMPLES,NO_OF_FEATURES+1))
Y=np.zeros((NO_OF_SAMPLES,1))
W=np.zeros((NO_OF_FEATURES,1))

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

##########################################
# Training and Testing
##########################################
kernel_gp=1000**2 * RBF(length_scale=70) 
gp=GaussianProcessRegressor(kernel=kernel_gp, alpha=0,optimizer=None, normalize_y=True)

accuracyMeasures=np.array([0, 0, 0, 0]);#TP,TN,FP,FN
for n_K in range(CROSS_VALIDATION_K):
    xTrain,yTrain,xTest,yTest=splitTrainingTestingData(X,Y,CROSS_VALIDATION_K,n_K)
    #print(xTrain.shape)
    #print(xTest.shape)
    w=trainLinerModel(xTrain,yTrain,gp)
    accuracyMeasures=accuracyMeasures+testLinearModel(xTest,yTest,gp)
    
##########################################
# Performance Measurements
##########################################

TP,TN,FP,FN=accuracyMeasures
TRP=TP/(TP+FN)*100
SPC=TN/(TN+FP)*100
PPV= TP/(TP+FP)*100
NPV=TN/(TN+FN)*100
ACC=(TP+TN)/(TP+TN+FP+FN)*100
    
##########################################
# Display results
##########################################    
print("Sensitivity= "+str(TRP)+"%")
print("Specificity= "+str(SPC)+"%")
print("PPV= "+str(PPV)+"%")
print("NPV= "+str(NPV)+"%")
print("Accuracy= "+str(ACC)+"%")



