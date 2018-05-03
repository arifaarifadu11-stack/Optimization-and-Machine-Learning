# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 2
Gaussian Process
wisconsin breast cancer database used 

@author: KMShihab
"""


from utilityFunctions import trainGPModel,testGPModel
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, RationalQuadratic

def runGPModel(xTrain,yTrain,xTest,yTest,kernel_type):
    
    #########################################
    # optimum kernel params (from prvious milestones)
    #########################################
    if kernel_type=='RBF':
        RBF_scale=4.6416
        RBF_magnitude=10.0
        
    if kernel_type=='RationalQuadratic':
        RQ_scale=1.0
        RQ_alpha=10.0
         
    ##########################################
    # Training and Testing
    ##########################################
    if kernel_type=='RBF':
        kernel_gp=RBF_magnitude* RBF(length_scale=RBF_scale) 
    
    if kernel_type=='RationalQuadratic':
        kernel_gp=RationalQuadratic(alpha=RQ_alpha,length_scale=RQ_scale)
        
    gp=GaussianProcessClassifier(kernel=kernel_gp)
    
    
    trainGPModel(xTrain,yTrain.ravel(),gp)
    TP,TN,FP,FN=testGPModel(xTest,yTest,gp)
        
        
    ##########################################
    # Performance Measurements
    ##########################################
    
   
    ACC=(TP+TN)/(TP+TN+FP+FN)*100
        
    return ACC
    
    
    
