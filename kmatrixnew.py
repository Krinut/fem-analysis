#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

import numpy as np
from kmatrix import *
from coordinates import elementno, nodesno

#this file is used to create a K matrix of dimension NxN where N = number of nodes*2.
#This file takes the K matrix as the input and adds columns and rows of zeros to the matrix to find the final K matrix

knew = []
dknew = []
count = 0
for i in range(0, elementno):
    #dknew.append(K[i])
    arr1 = np.vstack((np.zeros(((2*i),6)),K[i]))
    #print(arr1)
    arr2 = np.vstack((arr1, np.zeros(((2*nodesno-6-2*i),6))))
    #print(arr2)
    arr3 = np.hstack((np.zeros((2*nodesno,2*i)),arr2))
    #print(arr3)
    arr4 = np.hstack((arr3, np.zeros((2*nodesno,2*nodesno-6-2*i))))
    #print(arr4)
    knew.append(arr4)

for i in range(0, elementno):
    print("\nnew K{} matrix".format(i))
    print(knew[i])
