#read the passwords.txt file
with open('passwords6.txt') as f:
    lines=f.read().splitlines()

#print(lines)
print(len(lines))
#n=len(lines) #number of keys from passwords.txt

def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]: #goes through the linked list
            print("-->", end = " ")
            print(j, end = " ")
              
        print()


#key every time so we can easily look up the value instead of using a forloop
def djb2(stringinput,HashTable):
    #return hash(stringinput) % len(HashTable)
    hash=5381
     #for every letter in the string
    for c in stringinput:
         hash=(hash*33)+ord(c)
    return hash % len(HashTable)

#create hashtable as a nested list
HashTable = [[] for _ in range(len(lines)+8000)]
# the _ means we don't care about iterator value,we could have used a variable
#even if table has m=n, there is chance of remaping


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    #!assuming the key value is just the index of the value in lines
    Hashtable[keyvalue].append(value)
  
# MAIN FUNCTION
def load_table(HashTable,lines):
    #LOADING HASH TABLE WITH VALUES FROM PASSWORD.TXT
    for i in range(len(lines)):
            key=djb2(lines[i],HashTable)
            insert(HashTable,key,lines[i])

    display_hash(HashTable) 

def check_exist(string, HashTable):
    temp_key=djb2(string,HashTable)  #creates key for string
    
    # index into hash table with temp_key
    if (len(HashTable[temp_key])==0): #if linkedlist is empty
        return False #password doesn't exist
        

    else: #greater than 1 means it has a linked list
        for g in HashTable[temp_key]:
            print(g)
            if (string==g):
                return True #password exists therefore not valid

        return False #if you go through the linkedlist and nothing is matched then return True


def check_pass(string, HashTable,lines):
    #check alphanumeric, and between 6-12 characters
    if (string.isalnum() and len(string)<=12 and len(string)>=6):
        inverse=string[::-1] #creates a reversed string
        print(inverse)
        if check_exist(string, HashTable) or check_exist(inverse,HashTable): #if both exist --> invalid
            print("INVALID")

        else:
            print("VALID")
            keyvalue=djb2(string,HashTable)  #creates key for string
            
            insert(HashTable, keyvalue, string)
            print(keyvalue,HashTable[keyvalue])
    else:
        print('INVALID') 
        


#LOADS PASSWORD FILE
load_table(HashTable,lines)
collisioncounter=0

for i in HashTable:
    if len(i)>1:
        collisioncounter+= len(i)-1

print('number of collissions is',collisioncounter)


#check_pass('123456',HashTable,lines)

#TESTING
#WIx33Fn
#nF33xIW
#source of code https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/