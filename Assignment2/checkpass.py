#source of code https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/

#read the passwords.txt file
with open('passwords.txt') as f:
    lines=f.read().splitlines()

print(lines)
print(len(lines))
n=len(lines) #number of keys from passwords.txt

#chained hash table implementation python
#n keys, but m slots
# load factor = n/m = keys/slots

def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()



#! is it okay to make the hash table the same size as the passwords file? I thought we were suppoesd to make smaller
# for Q2 we need to vary size of table given an input of 1000 so it cnanot always be that way

# Hashing Function to return 
# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

#create hashtable as a nested list
HashTable = [[] for _ in range(len(lines)-200)]
# the _ means we don't care about iterator value,we could have used a variable 

dic={}
for i in range(len(lines)):
    dic[i]=None

#print(dic)

# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    #!assuming the key value is just the index of the value in lines
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
  
# MAIN FUNCTION
def load_table(HashTable,lines):
    

    #LOADING HASH TABLE WITH VALUES FROM PASSWORD.TXT
    for i in range(len(lines)):
            insert(HashTable,i,lines[i])

    display_hash (HashTable)

#load_table(HashTable,lines)

def check_pass(string, HashTable,lines):
    #check alphanumeric, and between 6-12 characters
    if (string.isalnum() and len(string)<=12 and len(string)>=6):

        
        print ('yes')

check_pass("HATEece123!",HashTable,lines)

  
