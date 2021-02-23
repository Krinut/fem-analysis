#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this file is used to check the direction in which nodes are taken (to be taken counter clockwise)

import numpy as np
from coordinates import *

#function to check the order of coordinates for each element
def check(i):
    if i%2==0:
        x1=Cx[i]
        x2=Cx[i+1]
        x3=Cx[i+2]
        y1=Cy[i]
        y2=Cy[i+1]
        y3=Cy[i+2]

    else:
        x1=Cx[i]
        x2=Cx[i+2]
        x3=Cx[i+1]
        y1=Cy[i]
        y2=Cy[i+2]
        y3=Cy[i+1]

    return [x1,y1,x2,y2,x3,y3]
