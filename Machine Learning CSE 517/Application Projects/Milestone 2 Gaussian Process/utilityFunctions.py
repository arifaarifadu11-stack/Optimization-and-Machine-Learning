# -*- coding: utf-8 -*-
"""
uitility Functions for Implementation project 

@author: Shihab
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, RationalQuadratic

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
    
    
    Ytrain1=Y[0:n_K*sampleSize]
    Ytest=Y[n_K*sampleSize:(n_K+1)*sampleSize]
    Ytrain2=Y[(n_K+1)*sampleSize:]
    if Ytrain1.size:
        if Ytrain2.size:
            Ytrain=np.concatenate([Ytrain1,Ytrain2])
        else:
            Ytrain=Ytrain1
    else:
        Ytrain=Ytrain2
    
    return Xtrain,Ytrain,Xtest,Ytest
    
    
    
    
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

def getBestParametersRBF(X,Y):
    nMag=10
    nScale=10
    nValidation=2
    magnitudes=np.logspace(-2,4,nMag)
    scales=np.logspace(-1,2,nScale)
    nlpd=np.zeros((nMag,nScale))
    for i in range(nMag):
        for j in range(nScale):
            sumProb=0.0
            numProb=0
            for n_k in range(nValidation):
                gp=GaussianProcessClassifier(kernel=magnitudes[i]* RBF(scales[j]))
                xTrain,yTrain,xTest,yTest=splitTrainingTestingData(X,Y,nValidation,n_k)
                gp.fit(xTrain,yTrain)
                probs=gp.predict_proba(xTest)
                sumProb+=sum(-np.log(probs[i][(1+yTest[i])//2]) for i in range(probs.shape[0]))
                numProb+=probs.shape[0]
            
            nlpd[i,j]=sumProb/numProb
                
            
    id_x,id_y=np.unravel_index(nlpd.argmin(), nlpd.shape)
    X,Y=np.meshgrid(magnitudes,scales)
    nlpd=np.transpose(nlpd)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(np.log10(X), np.log10(Y), nlpd, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=10)
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Length-scale")
    ax.set_zlabel("Negative Log Predictive Density")
    plt.show()
    
    return scales[id_y],magnitudes[id_x]

def getBestParametersRQ(X,Y):
    nAlpha=3
    nScale=3
    nValidation=2
    alphas=np.logspace(-1,1,nAlpha)
    scales=np.logspace(-1,2,nScale)
    nlpd=np.zeros((nAlpha,nScale))
    for i in range(nAlpha):
        for j in range(nScale):
            sumProb=0.0
            numProb=0
            for n_k in range(nValidation):
                gp=GaussianProcessClassifier(kernel=RationalQuadratic(alpha=alphas[i],length_scale=scales[j]))
                xTrain,yTrain,xTest,yTest=splitTrainingTestingData(X,Y,nValidation,n_k)
                gp.fit(xTrain,yTrain)
                probs=gp.predict_proba(xTest)
                sumProb+=sum(-np.log(probs[i][(1+yTest[i])//2]) for i in range(probs.shape[0]))
                numProb+=probs.shape[0]
            
            nlpd[i,j]=sumProb/numProb
                
            
    id_x,id_y=np.unravel_index(nlpd.argmin(), nlpd.shape)
    X,Y=np.meshgrid(alphas,scales)
    nlpd=np.transpose(nlpd)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(np.log10(X), np.log10(Y), nlpd, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=10)
    ax.set_xlabel("alpha")
    ax.set_ylabel("Length-scale")
    ax.set_zlabel("Negative Log Predictive Density")
    plt.show()
    
    return scales[id_y],alphas[id_x] #scale,alpha
    
        
