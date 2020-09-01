
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


class vertex:
    def __init__(self):
        self.visited = False
        self.d = 0
        self.parent = None

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]!=0:
            neigh.append(i)
    return neigh

def BFS(G,s,t,verticles):
    Q = queue()
    Q.enqueue(s)
    for i in range(len(verticles)):
        verticles[i].visited = False
    verticles[s].visited = True
    
    while not Q.is_empty():
        u = Q.dequeue()
        for v in neighbour(G,u):
            if (verticles[v].visited==False):
                verticles[v].visited = True
                verticles[v].d = verticles[u].d+1
                verticles[v].parent = u
                Q.enqueue(v)

    return verticles[t].visited


def maxFlow(G,sources, sinks):
    n = len(G)
    for i in range (2):
        G.append([0]*n)
    
    for i in range (n+2):
        G[i].append(0)
        G[i].append(0)

    s = len(G)-2
    t = len(G)-1

    for x in range(len(sources)):
        G[s][sources[x]] = float("inf")
    for y in range(len(sinks)):
        G[sinks[y]][t] = float("inf")


    fmax = 0
    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    
    while BFS(G,s,t,verticles):
        #dopoki istnieje sciezka rozszezajaca

        current = t
        curFlow = float("inf")

        
        while(current != s):
            if G[verticles[current].parent][current]<curFlow:
                curFlow = G[verticles[current].parent][current]
            current = verticles[current].parent

        fmax += curFlow

        temp = t

        while(temp != s):
            G[verticles[temp].parent][temp] -= curFlow
            G[temp][verticles[temp].parent] += curFlow
            temp = verticles[temp].parent

        
    

    return fmax

G = [[0,0,0,6,0,0,0,0], [0,0,0,0,0,0,0,7], [0,0,0,6,5,0,0,0], [0,0,0,0,10,4,0,0],
[0,0,0,0,0,0,2,8], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,5,0]]
sources = [0,1,2]
sinks = [5,6]

print(maxFlow(G,sources,sinks))
