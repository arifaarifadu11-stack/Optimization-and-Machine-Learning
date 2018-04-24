# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 1
Linear Model
wisconsin breast cancer database used 

@author: KMShihab
"""

import numpy as np
import timeit
from utilityFunctions import *
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, RationalQuadratic

#constant parameters
NO_OF_FEATURES=30
NO_OF_SAMPLES=569

#user defined parameters
CROSS_VALIDATION_K=10
kernel_type='RBF' # options :'RBF',  'RationalQuadratic'

#######################################
#for i-th sample
#X(i) is feature vector, Y(i) is label 
########################################
X=np.ones((NO_OF_SAMPLES,NO_OF_FEATURES+1))
Y=np.array([0]*NO_OF_SAMPLES)

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
Xvalidation=X[0:200,:]
Yvalidation=Y[0:200]
X=X[200:,:]
Y=Y[200:]

#########################################
# Optimal Parameter selection
#########################################
RBF_scale=1.0
RBF_magnitude=10.0
RQ_scale=1.0
RQ_alpha=10.0

if kernel_type=='RBF':
    RBF_scale,RBF_magnitude=getBestParametersRBF(Xvalidation,Yvalidation)
    print(' ')
    print('optimum RBF scale= '+str(RBF_scale))
    
if kernel_type=='RationalQuadratic':
    RQ_scale,RQ_alpha=getBestParametersRQ(Xvalidation,Yvalidation)
    print(' ')
    print('optimum RQ scale= '+str(RQ_scale))
    print('optimum RQ alpha= '+str(RQ_alpha))
     
##########################################
# Training and Testing
##########################################
if kernel_type=='RBF':
    kernel_gp=RBF_magnitude* RBF(length_scale=RBF_scale) 

if kernel_type=='RationalQuadratic':
    kernel_gp=RationalQuadratic(alpha=RQ_alpha,length_scale=RQ_scale)
    
gp=GaussianProcessClassifier(kernel=kernel_gp)

accuracyMeasures=np.array([0, 0, 0, 0]);#TP,TN,FP,FN
for n_K in range(CROSS_VALIDATION_K):
    xTrain,yTrain,xTest,yTest=splitTrainingTestingData(X,Y,CROSS_VALIDATION_K,n_K)
    #start = timeit.default_timer()
    trainGPModel(xTrain,yTrain,gp)
    #stop1 = timeit.default_timer()
    accuracyMeasures=accuracyMeasures+testGPModel(xTest,yTest,gp)
    #stop2 = timeit.default_timer()
    #print(stop1-start)
    #print(stop2-stop1)
    
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



