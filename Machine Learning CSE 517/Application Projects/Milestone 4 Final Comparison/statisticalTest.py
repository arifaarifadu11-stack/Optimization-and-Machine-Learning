# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 3
Dimensionality Reduction
wisconsin breast cancer database used 

@author: KMShihab
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

CROSS_VALIDATION_K=10
NO_OF_RUNS=10

# resultAll : for storing for all runs and cross-validations
#1st row: Linear without DR
#2nd row: Linear with DR
#3rd row: GP RBF without DR
#4th row: GP RBF with DR
#5th row: GP RQ without DR
#6th row: GP RQ with DR
resultAll=np.zeros((6,CROSS_VALIDATION_K*NO_OF_RUNS))

for nRun in range(NO_OF_RUNS):
    fileName='resultRun'+str(nRun+1)+'.txt'
    lines = [line.rstrip('\n') for line in open(fileName)]
    for lineIndex in range(len(lines)):
        resultAll[lineIndex,nRun*CROSS_VALIDATION_K:(nRun+1)*CROSS_VALIDATION_K]=list(map(float,lines[lineIndex].split()))
        

for i in range(6):
    for j in range(6):
        t,p=stats.ttest_rel(resultAll[j,:],resultAll[i,:])
        print('{0:.3f}'.format(p),end=' ')
        print('{0:.3f}'.format(t),end='\t')
    print('\n')

"""
fValue,pValue=stats.f_oneway(resultAll[0,:],resultAll[1,:],resultAll[2,:],resultAll[3,:],resultAll[4,:],resultAll[5,:])
print(fValue)
print(pValue)
"""














