#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this file calculates the final K matrix by adding all the updated K matrices.

import numpy as np
from kmatrix import *
from coordinates import nodesno, elementno

from kmatrixnew import *
K_total = np.zeros((2*nodesno, 2*nodesno))
for i in range(0, elementno):
    K_total = np.add(K_total, knew[i])

print("\Total K matrix:")
print(K_total)
print(np.linalg.det(K_total))
