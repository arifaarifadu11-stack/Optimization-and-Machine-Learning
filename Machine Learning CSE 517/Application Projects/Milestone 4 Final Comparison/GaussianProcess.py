# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 2
Gaussian Process
wisconsin breast cancer database used 

@author: KMShihab
"""

import numpy as np
import time
from utilityFunctions import splitTrainingTestingData,trainGPModel,testGPModel
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, RationalQuadratic

def runGPModel(X,Y,CROSS_VALIDATION_K,kernel_type,kernel_params):
    start_time=time.clock()
    #########################################
    #unpacking kernel params
    #########################################
    
    if kernel_type=='RBF':
        RBF_scale,RBF_magnitude=kernel_params
        
    if kernel_type=='RationalQuadratic':
        RQ_scale,RQ_alpha=kernel_params
         
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
        trainGPModel(xTrain,yTrain.ravel(),gp)
        accuracyMeasures=accuracyMeasures+testGPModel(xTest,yTest,gp)
        
        
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
    
    
    
