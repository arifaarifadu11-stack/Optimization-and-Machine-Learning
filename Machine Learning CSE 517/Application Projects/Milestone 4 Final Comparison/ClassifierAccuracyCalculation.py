# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 4
Accuracy calculation for all previous classifiers studied
 for wisconsin breast cancer database

@author: KMShihab
"""
import numpy as np
from sklearn.decomposition import PCA
from LinearModel import runLinearModel
from GaussianProcess import runGPModel
from utilityFunctions import splitTrainingTestingData
#Constant parameters
NO_OF_FEATURES=30
NO_OF_SAMPLES=569
CROSS_VALIDATION_K=10

#######################################
#for i-th sample
#X(i) is feature vector, Y(i) is label 
########################################
X=np.ones((NO_OF_SAMPLES,NO_OF_FEATURES))
Y=np.zeros((NO_OF_SAMPLES,1))

##########################################
# Reading file and formatting data
##########################################
fileInput = open('wdbc.data', 'r')
indexSample=0
for line in fileInput:
    data=line.split(',')
    #data[0] is patient ID
    features=list(map(float,data[2:]))
    # 1 for malignant tumor, -1 for benign tumor
    label=1 if data[1]=='M' else -1
    
    X[indexSample,:]=features
    Y[indexSample]=label
    indexSample+=1
       
fileInput.close()

##########################################
# dimensionality reduction
##########################################

#pca=PCA()
#pca.fit(X)
#print(pca.explained_variance_ratio_[:5])
#d=np.argmax(np.cumsum(pca.explained_variance_ratio_)>=0.99)+1
#pca=PCA(n_components=d)

pca=PCA(n_components=0.99)
X_reduced=pca.fit_transform(X)


##########################################
# calculate accuracy for all classifiers
##########################################

# resultAll contains accuracy for k fold cross vaidation
#1st row: Linear without DR
#2nd row: Linear with DR
#3rd row: GP RBF without DR
#4th row: GP RBF with DR
#5th row: GP RQ without DR
#6th row: GP RQ with DR
resultAll=np.zeros((6,CROSS_VALIDATION_K))


for n_K in range(CROSS_VALIDATION_K):
    
    #original dataset
    xTrain,yTrain,xTest,yTest=splitTrainingTestingData(X,Y,CROSS_VALIDATION_K,n_K)
    
    lamda=0.1
    resultAll[0][n_K]=runLinearModel(xTrain,yTrain,xTest,yTest,lamda) 
    kernel_type='RBF'
    resultAll[2][n_K]=runGPModel(xTrain,yTrain,xTest,yTest,kernel_type)
    kernel_type='RationalQuadratic'
    resultAll[4][n_K]=runGPModel(xTrain,yTrain,xTest,yTest,kernel_type)
    
    #reduced dataset
    xTrain,yTrain,xTest,yTest=splitTrainingTestingData(X_reduced,Y,CROSS_VALIDATION_K,n_K)
    
    lamda=0.1
    resultAll[1][n_K]=runLinearModel(xTrain,yTrain,xTest,yTest,lamda) 
    kernel_type='RBF'
    resultAll[3][n_K]=runGPModel(xTrain,yTrain,xTest,yTest,kernel_type)
    kernel_type='RationalQuadratic'
    resultAll[5][n_K]=runGPModel(xTrain,yTrain,xTest,yTest,kernel_type)
    

with open('resultRun.txt','w') as fileOutput:
    for i in range(6):
        fileOutput.write('\t'.join(map(str,resultAll[i,:]))+'\n')
    
    

















