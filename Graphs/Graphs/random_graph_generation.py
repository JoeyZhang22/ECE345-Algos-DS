#! /usr/bin/env python3
import numpy as np
from random import randint
from random import random

# open function to create new text file and set mode to write
f = open("graph10_1000edges.txt", "w")

density_ratio = 10 # for generating graphs of different densities(#edges/#nodes) range[2:10]

for i in range (0,density_ratio*100):

    node1 = randint(0,100)
    node2 = randint(0,100)
    while node2 == node1:
        node2 = randint(0,100)
    
    #Randomly generate weight from values 0 to 5
    weight = round(np.random.uniform(0,5),6) #rounding number to 6 decimal places

    f.write(str(node1) + " " + str(node2) + " " + str(weight) + "\n")