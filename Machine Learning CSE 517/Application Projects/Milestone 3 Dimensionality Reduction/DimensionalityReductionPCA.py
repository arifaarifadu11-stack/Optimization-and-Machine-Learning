# -*- coding: utf-8 -*-
"""
Implementation project
Milestone 3
Dimensionality Reduction
wisconsin breast cancer database used 

@author: KMShihab
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from sklearn.decomposition import PCA

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

#pca=PCA()
#pca.fit(X)
#d=np.argmax(np.cumsum(pca.explained_variance_ratio_)>=0.99)+1
#pca=PCA(n_components=d)


##########################################
# data visualization
##########################################
pca=PCA(n_components=0.99)
X_reduced=pca.fit_transform(X)

plot_x=X_reduced[:,0]
plot_y=X_reduced[:,1]

benignX=np.array([X_reduced[i][0] for i in range(NO_OF_SAMPLES) if Y[i]==-1])
benignY=np.array([X_reduced[i][1] for i in range(NO_OF_SAMPLES) if Y[i]==-1])
plt.scatter(benignX, benignY, s=None, marker='+', c="k")

malignantX=np.array([X_reduced[i][0] for i in range(NO_OF_SAMPLES) if Y[i]==1])
malignantY=np.array([X_reduced[i][1] for i in range(NO_OF_SAMPLES) if Y[i]==1])
plt.scatter(malignantX, malignantY, s=None, marker='+', c="r")

plt.show()


















