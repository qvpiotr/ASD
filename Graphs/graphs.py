# graphs representation
#V = input("vertices")
V = 8
#adjacency matrix representation
#Aij = 1 when there is an edge from vertex i to vertex j
#Aij = 0 when there is no edge


A = [['0' for _ in range(V)] for _ in range(V)]

#adjency list representation

class Node:
    def __init__(self):
        self.val = None
        self.next = None


def add(head, x):
    tmp = Node()
    tmp.val = x
    temp = Node()
    temp = head
    if temp == None: temp.next = tmp
    else:
        while(temp.next != None):
            temp = temp.next
        temp.next = tmp
        
L = [Node() for _ in range(V)]
##########
add(L[0],2)
add(L[2],3)
add(L[2],4)



