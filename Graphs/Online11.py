#METODA FORDA FULKERSONA
#metoda polega na zwiekszaniu wartosci przepływu
#dopóki istnieje ścieżka powiększająca w sieci
#resydualnej

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


def maxFlow(G,s,t):
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


c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
print( maxFlow( c, 0, 3 ) ) # wypisze 3





