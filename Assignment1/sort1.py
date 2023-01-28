#! /usr/bin/env python3
#Insertion sort [Joey]
import sys #system commands for taking input form terminal
import csv #for opening csv file
import time #timing function for algo

def csv_opener(csv_file):
    data = [] #convert csv_file data into list 

    with open (csv_file) as file:
        csv_generated_object = csv.reader(csv_file)
        for row in csv_generated_object:
            data.append(row)

    return data

def csv_opener_local():
    data = []
    with open("a1.small.csv") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            #print(row)
            data.append(row)
    
    return data

def insertion_sort(list): #input list
    for i in range(1, len(list)):
        #print(i)
        (sort_key, temp) =(list[i][0],list[i])
        j=i-1 
        while j>=0:
            if int(list[j][0])< int(sort_key): # because csv data is in strings --> type cast to integer
                break #sort_key is larger than previous element --> nothing needs to change
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp



#testing the code for sorting
input_argument= sys.argv[1] + ".csv"
print ("the input is: ",input_argument)
list = csv_opener_local()
#print original list
for i in range(0,len(list)):
    print(list[i])
new_list=insertion_sort(list)

print(len(list))
#print(list)

for i in range(0,len(list)):
    print(list[i])

#sort list



