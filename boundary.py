#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

import numpy as np
from totalkmatrix import *

#calcK = np.concatenate((K_total[:,0], K_total[:,1], K_total[:,4], K_total[:,5], K_total[:,6]), axis=1) #sir example
calcK = np.concatenate((K_total[:,4], K_total[:,5], K_total[:,6], K_total[:,7]), axis=1)    #cantiliver
#print(K_total[:,0])
print(calcK)
#calcK2 = np.concatenate((calcK[0,:], calcK[1,:], calcK[4,:], calcK[5,:], calcK[6,:]), axis=0)  #sir exampple
calcK2 = np.concatenate((calcK[4,:], calcK[5,:], calcK[6,:], calcK[7,:]), axis=0)  #cantiliver

print(np.matrix(calcK2))
print(np.linalg.inv(calcK2))
#U = np.matmul(np.linalg.inv(calcK2), np.matrix([[1], [1], [0], [0], [0]])) #sir example
U = np.matmul(np.linalg.inv(calcK2), np.matrix([[0], [-20], [0], [0]]))

print(U)
