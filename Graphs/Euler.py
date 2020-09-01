#adjacency matrix representation

#A - graph, S - start vertex

class Node:
    def __init_(self):
        self.next = None
        self.val = None

class Stack:
    def __init__(self):
        self.top = Node()  # wartownik
        self.top.next = None

    def push(self, x):
        N = Node()
        N.val = x
        N.next = self.top.next
        self.top.next = N

    def pop(self):
        N = self.top.next
        self.top.next = N.next
        return N.val

    def is_empty(self):
        return self.top.next == None
        
def printStack(stack):
        x = stack.top.next
        while not x == None:
            y = stack.pop()
            print(y, end = ' ')
            x = x.next
        

class vertex:
    def __init__(self):
        self.edges = []
        self.degree = len(self.edges)

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]==1:
            neigh.append(i)
    return neigh

time = 0
def Euler(G):

    def DFSVisit(u):
       
        for v in neighbour(G, u):
            for i in range (len(verticles[u].edges)):
                if not verticles[u].edges: break
                if verticles[u].edges[i] == v:
                    stack.push(v)
                    verticles[u].edges.remove(v)
                    verticles[v].edges.remove(u)
                    DFSVisit(v)  
        
        x = stack.pop()
        res.push(x)
         

    stack = Stack()
    res = Stack()
    verticles = []
    for i in range (len(G)):
        verticles.append(vertex())
        verticles[i].edges = neighbour(G,i)
        verticles[i].degree = len(verticles[i].edges)
        if verticles[i].degree %2 != 0: return
    for v in range(len(G)):
        while verticles[v].edges:
            stack.push(v)
            DFSVisit(v)
    return res

G = [[0,1,0,1,1,1], [1,0,1,1,1,0], [0,1,0,1,0,0], [1,1,1,0,0,1],[1,1,0,0,0,0], [1,0,0,1,0,0]]
printStack(Euler(G))