#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this file calculates the displacement matrices based on the force input by the user

import numpy as np
from totalkmatrix import *
from coordinates import nodesno, elementno

tip_force = float(input("\nPlease input the tip force: "))
forcemat = np.array([0])
calcK2 = K_total[4:nodesno*2, 4:nodesno*2]
#print(calcK2)

for i in range(5, nodesno*2):
    forcemat = np.concatenate((forcemat,np.array([0])), axis=0)
#print(forcemat)

if elementno%2==0:
    forcemat[nodesno*2-7]=tip_force
else:
    forcemat[nodesno]=tip_force

#print(forcemat)
U = np.matmul(np.linalg.inv(calcK2), np.transpose(np.matrix(forcemat)))

print("\ndisplacement matrix: ")
print(U)
