#! /usr/bin/env python3
import sys
#DISPLAY HASH_TABLE
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]: #goes through the linked list
            print("-->", end = " ")
            print(j, end = " ")
              
        print() #prints blank line for formatting

#DJB2: generic hashing function --> makes use of simple multiplication and unicoding for characters. Created by dan bernstein from http://www.cse.yorku.ca/~oz/hash.html
def djb2(stringinput,HashTable):
    #return hash(stringinput) % len(HashTable)
    hash=5381
     #for every letter in the string
    for c in stringinput:
         hash=(hash*33)+ord(c) #ord returns unicode for character
    return hash % len(HashTable) 

# INSERT Function
def insert(Hashtable, keyvalue, value):
    #!assuming the key value is just the index of the value in lines
    Hashtable[keyvalue].append(value)
  
# LOAD Table
def load_table(HashTable,lines):
    #LOADING HASH TABLE WITH VALUES FROM PASSWORD.TXT
    for i in range(len(lines)):
            key=djb2(lines[i],HashTable)
            insert(HashTable,key,lines[i])

    display_hash(HashTable) 

# CHECK existence of password
def check_exist(string, HashTable):
    temp_key=djb2(string,HashTable)  #creates key for string
    
    # index into hash table with temp_key
    if (len(HashTable[temp_key])==0): #if linkedlist is empty
        return False #password doesn't exist
        

    else: #greater than 1 means it has a linked list
        for g in HashTable[temp_key]:
            if (string==g):
                return True #password exists therefore not valid

        return False #if you go through the linkedlist and nothing is matched then return True

#CHECK if reverse and original Password exist
def check_pass(string, HashTable):
    #check alphanumeric, and between 6-12 characters
    if (string.isalnum() and len(string)<=12 and len(string)>=6):
        inverse=string[::-1] #creates a reversed string
        if check_exist(string, HashTable) or check_exist(inverse,HashTable): #if both exist --> invalid
            print("INVALID")
            return False #don't insert

        else:
            print("VALID")
            keyvalue=djb2(string,HashTable)  #creates key for string
            
            insert(HashTable, keyvalue, string)
            return True #insert
    else:
        print('INVALID') 
        return False
        


#main of the file

if(len(sys.argv)!=3):
    print("not enough input arguments")

else:
    password_txt_file= sys.argv[1] 
    password_to_check=sys.argv[2]

    with open(password_txt_file) as f:
        lines=f.read().splitlines()

    #create hashtable as a nested list
    HashTable = [[] for _ in range(len(lines))]
    load_table(HashTable,lines)

    #check if it exists or not then insert into text file
    if(check_pass(password_to_check,HashTable)==True):
        txt_file = open(password_txt_file, 'a')
        txt_file.write(password_to_check + "\n")

#sources used: https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/