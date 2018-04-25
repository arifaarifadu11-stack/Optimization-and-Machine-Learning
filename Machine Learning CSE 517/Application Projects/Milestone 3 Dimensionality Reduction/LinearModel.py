# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 1
Linear Model
wisconsin breast cancer database used 

@author: KMShihab
"""

import numpy as np
import time
from utilityFunctions import splitTrainingTestingData,trainLinerModel,testLinearModel


def runLinearModel(X,Y,lamda,CROSS_VALIDATION_K):
    start_time=time.clock()
    ##########################################
    # Training and Testing
    ##########################################
    accuracyMeasures=np.array([0, 0, 0, 0]) #TP,TN,FP,FN
    for n_K in range(CROSS_VALIDATION_K):
        xTrain,yTrain,xTest,yTest=splitTrainingTestingData(X,Y,CROSS_VALIDATION_K,n_K)
        #print(xTrain.shape)
        #print(xTest.shape)
        w=trainLinerModel(xTrain,yTrain,lamda)
        accuracyMeasures=accuracyMeasures+testLinearModel(xTest,yTest,w)
        
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
    
    end_time=time.clock()
    print('execution time= '+"{:0.6f}".format(end_time-start_time))



