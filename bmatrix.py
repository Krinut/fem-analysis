#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this file calculates the B matrices for each element

import numpy as np
from coordinates import *
from checker import *
from area import *
B = [] #B matrix

for i in range(0, elementno):
    x1,y1,x2,y2,x3,y3 = check(i)
    Bdraft = (1/(2*a[i]))*np.matrix([[y2-y3,0,y3-y1,0,y1-y2,0], [0,x3-x2,0,x1-x3,0,x2-x1], [x3-x2,y2-y3,x1-x3,y3-y1,x2-x1,y1-y2]])
    print(x1,y1,x2,y2,x3,y3)
    B.append(Bdraft)

for i in range(0, elementno):
    print("\nB[{}] matrix".format(i))
    print(B[i])
