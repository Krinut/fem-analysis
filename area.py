#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#This file calculates and stores the area of each element

import numpy as np
from coordinates import *
from checker import *
a = [] #list for area of all the elements

for i in range(0, elementno):
    x1,y1,x2,y2,x3,y3 = check(i)
    area = 0.5*np.linalg.det(np.matrix([[1, x1, y1], [1,x2,y2], [1,x3,y3]]))
    a.append(area)

for i in range(0, elementno):
    print("\nArea of {}th element".format(i))
    print(a[i])
