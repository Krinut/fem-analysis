#!usr/bin/env python3

#Author: Krishna SOni
#FEM on cantiliver beam

#this file calculates and stores the coordinates of each element based on the number of elements entered

L = float(input("Enter the length: "))  #length of the bar
H = float(input("Enter the height: ")) #heigth of the bar
elementno = int(input("Enter number of elements: "))    #number of elements
nodesno = elementno + 2 #number of nodes = number of elements + 2
V = float(input("Enter Poisson's ratio: "))
E = float(input("Enter Young's Modulus: "))

#from final import L, H, elementno, nodesno

#lists for coordinates
Cx = [0,0] #list for x coordintes
Cy = [] #list for y coordinates

#finding out the coordinates for each node
for i in range(2, nodesno-1):
    Cx.append(((i-1)*L)/(elementno-1))  #just appending the values of new coordinates
Cx.append(L) #add the last node

for i in range(0,nodesno):
    if i%2==0:
        Cy.append(H)
    else:
        Cy.append(0)
print("Coordinates matrix")
print(Cx, Cy)
