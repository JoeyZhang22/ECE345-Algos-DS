from random import randint
from random import random

if __name__ == "__main__":
    f = open("textnode_10.txt", "w")

    edge = randint(2,10)

    for i in range (0,edge*100):

        node1 = randint(0,100)
        node2 = randint(0,100)
        while node2 == node1:
            node2 = randint(0,100)
        weight = round(random.uniform(0,5),6)

        f.write(str(node1) + " " + str(node2) + " " + str(weight) + "\n")