# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 23:13:38 2018

@author: KMShihab
"""

import numpy as np
import random
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, RationalQuadratic
from scipy import linalg as linearAlgorithm

def splitTrainingTestingData(X,Y,CROSS_VALIDATION_K,n_K):
    nSamples,nFeatures=X.shape
    testSize=nSamples//CROSS_VALIDATION_K
    
    #radomize the rows
    randomIndices=random.sample(range(nSamples),nSamples)
    
    Xtest=X[randomIndices[:testSize],:]
    Xtrain=X[randomIndices[testSize:],:]
    
    Ytest=Y[randomIndices[:testSize]]
    Ytrain=Y[randomIndices[testSize:]]
    
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


def trainGPModel(Xtrain,Ytrain,gp):
    gp.fit(Xtrain,Ytrain)


def testGPModel(Xtest,Ytest,gp):
    TP=0    #True positive
    TN=0    #True Negative
    FP=0    #False positive
    FN=0    #False negative
    
    nSamples,nFeatures=Xtest.shape
    predictions=gp.predict(Xtest)
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