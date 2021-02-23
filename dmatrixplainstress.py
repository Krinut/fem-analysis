#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this file calculates the D matrix for plain stress condition

import numpy as np
from coordinates import V,E

#from final import V,E

Dstress = (E/((1+V)*(1-V)))*np.array([[1, V, 0], [V, 1, 0], [0, 0, (1-V)/2]])

print("\nDstress matrix:")
print(Dstress)
#print(D[0][1])
