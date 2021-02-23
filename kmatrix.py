#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

import numpy as np
from area import *
from bmatrix import *
from dmatrix import *
from coordinates import elementno
from dmatrixplainstress import *

#this file calculates the K matrix for each element

K = [] #list for K matrix
choice = int(input("\nPress 1 for plain strain and 2 for plain stress: "))
if choice == 1:
    for i in range(0, elementno):
        draft1 = np.matmul(D,B[i])
        draft2 = np.matmul(np.transpose(B[i]), draft1)
        draft3 = a[i]*draft2

        K.append(draft3)
else:
    for i in range(0, elementno):
        draft1 = np.matmul(Dstress,B[i])
        draft2 = np.matmul(np.transpose(B[i]), draft1)
        draft3 = a[i]*draft2

        K.append(draft3)

for i in range(0, elementno):
    print("\nK[{}] matrix".format(i))
    print(K[i])
    print("Determinant",np.linalg.det(K[i]))
    #print(np.transpose(K[i]))
