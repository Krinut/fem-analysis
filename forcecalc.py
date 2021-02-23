#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this is the main file that the user has to run. It calculates the force matrix

import numpy as np

from boundary2 import U
from totalkmatrix import K_total
Udraft = np.concatenate((np.array([[0], [0], [0], [0]]),U), axis=0)
F = np.matmul(K_total, Udraft)

print("\nForce matrix: ")
print(F)
