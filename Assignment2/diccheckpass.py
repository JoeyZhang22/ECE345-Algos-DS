#source of code https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/

#read the passwords.txt file
with open('passwords.txt') as f:
    lines=f.read().splitlines() #not same as readlines which includes the \n after

#print(lines)
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()


# Hashing Function to return 
# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

#create hashtable as a nested list
HashTable = [[] for _ in range(len(lines)-200)]
# the _ means we don't care about iterator value,we could have used a variable 


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

def check_pass(string, dic,lines):
    #check alphanumeric, and between 6-12 characters
    if (string.isalnum() and len(string)<=12 and len(string)>=6):

        if (dic.get(string) is not None):
            print ('yes')

#check_pass("HATEece123!",HashTable,lines)

def hash_function(keyvalue):
    return keyvalue % len(dic)

#INSERT LINES INTO DICTIONARY
def dic_insert(dic,keyvalue,value):
    hash_key=hash_function(keyvalue)
    dic[keyvalue]=value

#create empty dictionary/hashtable
dic={}
for i in range(len(lines)):
    dic[i]=None

for j in range(len(lines)):
    dic_insert(dic,j,lines[j])
    #!problem is that it's also entering the \n in the dictionary

#print(dic.get("HATEece123!"))
print(dic)
print(dic.get(249))
#check_pass("miCmYXnEGsm", dic,lines)  
#print(dic)
#print (len(dic))
print(list(dic.keys())[list(dic.values()).index('miCmYXnEGs')])
