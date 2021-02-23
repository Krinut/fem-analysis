#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this file calculates the D matrix for plain strain condition

import numpy as np
from coordinates import V,E

#from final import V,E

D = ((E*(1-V))/((1+V)*(1-2*V)))*np.array([[1, V/(1-V), 0], [V/(1-V), 1, 0], [0, 0, (1-2*V)/(2*(1-V))]])

print("\nD matrix:")
print(D)
#print(D[0][1])
