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
        

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s[0]][i]>0:
            neigh.append(i)
    return neigh

def BFS(G, s):
    Q = queue()

    verticles=[]
    for _ in range (len(G)):
        verticles.append(vertex())
    
    verticles[s].visited = True
    Q.enqueue([s,0,0])

    while not Q.is_empty():
        u = Q.dequeue()

        if u[1] != 0:
            Q.enqueue([u[0],u[1]-1,u[2]+1])


        else:
            if verticles[u[0]].visited == False:
                verticles[u[0]].visited = True
                verticles[u[0]].d = u[2]

            for v in neighbour(G,u):
                if (verticles[v].visited==False):
                    Q.enqueue([v,G[u[0]][v]-1,u[2]+1])
            
    for i in range (len(verticles)):
        print(verticles[i].d)

G = [[0,3,0,0,0,4],[3,0,2,0,0,1],[0,2,0,3,0,2],[0,0,3,0,2,0],[0,0,0,2,0,1],[4,1,2,0,1,0]]
BFS(G,0)
