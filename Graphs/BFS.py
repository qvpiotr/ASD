#BFS breadth first search

class Node:
    def __init__(self):
        self.val = None
        self.next = None


class queue:
    def __init__(self):
        self.top = Node()
        self.top.next = None

    def enqueue(self, x):
        N = Node()
        N.val = x
        if queue.is_empty(self):
            self.top.next = N
        else:
            last = self.top
            while last.next:
                last = last.next
            last.next = N

    def dequeue(self):
        N = self.top.next
        self.top.next = N.next
        return N.val

    def is_empty(self):
        return self.top.next == None

#adjacency matrix representation

#A - graph, S - start vertex

class vertex:
    def __init__(self):
        self.visited = False
        self.d = 0
        self.parent = None

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]==1:
            neigh.append(i)
    return neigh

def BFS(G, s):
    Q = queue()
    verticles=[]
    for _ in range (len(G)):
        verticles.append(vertex())
    verticles[s].visited = True
    Q.enqueue(s)
    while not Q.is_empty():
        u = Q.dequeue()
        for v in neighbour(G,u):
            if (verticles[v].visited==False):
                verticles[v].visited = True
                verticles[v].d = verticles[u].d+1
                verticles[v].parent = u
                Q.enqueue(v)

G = [[0,1,0,0,1,1], [1,0,1,0,1,0], [0,1,0,1,0,0], [0,0,1,0,0,1],[1,1,0,0,0,0], [1,0,0,1,0,0]]
BFS(G,0)