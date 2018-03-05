# -*- coding: utf-8 -*-
"""
uitility Functions for Implementation project 

@author: Shihab
"""

import numpy as np
from scipy import linalg as linearAlgorithm

def splitTrainingTestingData(X,Y,CROSS_VALIDATION_K,n_K):
    nSamples,nFeatures=X.shape
    sampleSize=nSamples//CROSS_VALIDATION_K
    
    Xtrain1=X[0:n_K*sampleSize,:]
    Xtest=X[n_K*sampleSize:(n_K+1)*sampleSize,:]
    Xtrain2=X[(n_K+1)*sampleSize:,:]
    if Xtrain1.size:
        if Xtrain2.size:
            Xtrain=np.concatenate((Xtrain1,Xtrain2),axis=0)
        else:
            Xtrain=Xtrain1
    else:
        Xtrain=Xtrain2
    
    
    Ytrain1=Y[0:n_K*sampleSize,:]
    Ytest=Y[n_K*sampleSize:(n_K+1)*sampleSize,:]
    Ytrain2=Y[(n_K+1)*sampleSize:,:]
    if Ytrain1.size:
        if Ytrain2.size:
            Ytrain=np.concatenate((Ytrain1,Ytrain2),axis=0)
        else:
            Ytrain=Ytrain1
    else:
        Ytrain=Ytrain2
    
    return Xtrain,Ytrain,Xtest,Ytest
    
    
    
    
def trainLinerModel(Xtrain,Ytrain,lamda=0):
    nSamples,nFeatures=Xtrain.shape
    #Hessian Calculation
    H=np.dot(Xtrain.transpose(),Xtrain)+lamda*np.eye(nFeatures)
    # calculting X^T * Y
    XtY=np.dot(Xtrain.transpose(),Ytrain);
    #closed for solution to find w
    w=linearAlgorithm.solve(H,XtY)
    return w


def testLinearModel(Xtest,Ytest,w):
    TP=0    #True positive
    TN=0    #True Negative
    FP=0    #False positive
    FN=0    #False negative
    
    nSamples,nFeatures=Xtest.shape
    predictions=np.dot(Xtest,w)
    for i in range(nSamples):
        if Ytest[i]==1:
            if predictions[i]>=0:
                TP+=1   #Malignant; detected malignant
            else:
                FN+=1   #Malignant; detected Benign
        else:
            if predictions[i]>=0:
                FP+=1   #Benign; detected malignant
            else:
                TN+=1   #Benign; detected Benign
                
    return np.array([TP,TN,FP,FN])
