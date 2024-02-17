#! /usr/bin/env python3
#Heapsort

import numpy as np
from numpy import genfromtxt
import csv
import sys
import math
import time
#https://www.geeksforgeeks.org/building-heap-from-array/


def csv_opener(csv_file):
    data = [] #convert csv_file data into list 

    with open (csv_file) as file:
        csv_generated_object = csv.reader(file)
        for row in csv_generated_object:
            data.append(row)

    return data

def csv_opener_local(): #this one as different than previous one in the sense that you specify the file name, previous function you just fead it a csv and call it in terminal
    data = []
    with open("a1.large.csv") as file:
        csvreader = csv.reader(file)
        
        for row in csvreader: #converting csv into a list    
            data.append(row)

    return data



def heap_sort(A):
    
   #A=csv_opener_local() #loads a 2D list [[234,d,2,e,eight],[etc.]]
   # print(A)

    # record the time before running code
    start_time = time.time()
    buildmaxheap(A)
    heap_size=len(A)

    #!mistake i made was for i in range(heap_szie-1,-1) --> the for loop never runs
    #!another mistake was that I was not using a consistent heap_size value inside the heapsort,heapify function and build max heap
    #!since heap_size is being decreased, you cannot use the constant number
    for i in range(heap_size-1,0,-1): #starts from 0 to halfway of the array, if you got to end you undo all the swapping
        #perform a swap
        
       
        A[0],A[i]= A[i], A[0] #swap first and last element
        heap_size=heap_size-1
     
       
        heapify(A,0,heap_size) #we always call heapify on the root since the rest of the tree is correct
    end_time = time.time()
    #print((end_time-start_time)*1000)
    return(A)
       
#* heapify is good now
def heapify(A,j,heap_size):
    leftchild=2*j+1
    rightchild=2*j+2
    
    

    #!note: for python, it cnanot be less than or equal to, leftchild must be LESS than the heapsize, otherwise it will index
    #!outside of array
    
    #imagine that the array length is only 9, but when it calculates left child it will index position 9*2+1=19, which won't work
    if (leftchild <heap_size) and (int(A[leftchild][0])>int(A[j][0])):
            maximum=leftchild #we store the index
            #print(A[leftchild])
            #print('hit')
    else:
        maximum=j

    if (rightchild<heap_size) and (int(A[rightchild][0])>int(A[maximum][0])): 
        #!you don't compare to j again, you comapre to max, because if max is bigger than j then you are fucking yoursef
            maximum=rightchild #we store index
    #need to compare all 3 elements

    #if there's actually been a change ie the 3 elements are not a heap, fix it
    if (maximum !=j): #if the index of the maximum != the index of the parent
        A[j],A[maximum]= A[maximum], A[j] #do the swap to correct order
        #recursively call itself, starting at the index of the maximum since you know everything to the left of the max is properly sorted
        heapify(A,maximum,heap_size)

#* max heap also works
def buildmaxheap(A):
    heap_size=len(A)
    index=math.floor(heap_size/2) #you only need to do up to half of array length since you're calling heapify
    #rint(index)
    for k in range(index,-1,-1): # we index backwards from 5 to 1 because, we start at bottom of tree until we reach node
        #! not sure if it should index to 0
        
        heapify(A,k,heap_size)
        

#testing the code for sorting
input_argument= sys.argv[1] + ".csv"
print ("the input is: ",input_argument)
list = csv_opener(input_argument)
new_list=heap_sort(list)

for i in range(0,len(list)):
    print(list[i])