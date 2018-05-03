# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 1
Linear Model
wisconsin breast cancer database used 

@author: KMShihab
"""

from utilityFunctions import trainLinerModel,testLinearModel


def runLinearModel(xTrain,yTrain,xTest,yTest,lamda):
    
    ##########################################
    # Training and Testing
    ##########################################
    
    w=trainLinerModel(xTrain,yTrain,lamda)
    TP,TN,FP,FN=testLinearModel(xTest,yTest,w)
        
    ##########################################
    # Performance Measurements
    ##########################################
    ACC=(TP+TN)/(TP+TN+FP+FN)*100
        
    return ACC



