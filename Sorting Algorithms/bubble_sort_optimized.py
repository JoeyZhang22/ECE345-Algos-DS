#! /usr/bin/env python3
#Bubble sort [Joey]
import sys #system commands for taking input form terminal
import csv #for opening csv file
import time #timing function for algo

def csv_opener(csv_file):
    data = [] #convert csv_file data into list 

    with open (csv_file) as file:
        csv_generated_object = csv.reader(file)
        for row in csv_generated_object:
            data.append(row)

    return data

def csv_opener_local():
    data = []
    with open("a1.large.csv") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            #print(row)
            data.append(row)
    
    return data

def bubble_sort(list):
    #length of array
    n=len(list)
    #i: used to keep track of end range for y to travel
    #flag for swapping
    for i in range(0,n-1):
        swap= False
        for j in range(0, n-1-i):
            if int(list[j+1][0]) < int(list[j][0]):
                temp = list[j+1]
                list[j+1]=list[j]
                list[j]=temp
                
                #swap occured
                swap=True

        if(swap==False): #since no swap had occured at given iteration it means the list in its current form is already sorted
            break;   

    return list         

#testing the code for sorting
input_argument= sys.argv[1] + ".csv"
print ("the input is: ",input_argument)
list = csv_opener(input_argument)
#print original list
# for i in range(0,len(list)):
#     print(list[i])
start_time = time.time()
new_list=bubble_sort(list)
end_time = time.time()

for i in range(0,len(list)):
    print(list[i])

print("Time for Optimized Bubble Sort: ", 1000*(end_time-start_time))


# bubble sort guide: https://www.programiz.com/dsa/bubble-sort
