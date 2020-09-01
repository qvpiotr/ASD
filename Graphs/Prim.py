#algorytm Prima 
#MST


from queue import PriorityQueue

class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.d = float("inf")
        

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]>0:
            neigh.append(i)
    return neigh

def prim(G,s):
    q = PriorityQueue()

    verticles = []
    for v in range (len(G)):
        verticles.append(vertex())
    verticles[s].d =0

    for v in range (len(G)):
        q.put((float("inf"), v))
    
    while not q.empty():
        u = q.get()
        for v in neighbour(G,u[1]):
            if verticles[v].d > G[u[1]][v] and verticles[v].visited==False:
                verticles[v].d = G[u[1]][v]
                q.put((verticles[v].d, v))
                verticles[v].parent = u[1]
                verticles[v].visited = True
    MST = []

    for v in verticles:
        if v.parent is not None:
            MST.append((v.parent, verticles.index(v)))
    return MST

G = [[0,2,0,1,6,0,0],[2,0,3,0,0,0,0],[0,3,0,2,0,0,1],
[1,0,2,0,0,5,0],[6,0,0,0,0,8,0],[0,0,0,5,8,0,7],[0,0,1,0,0,7,0]]

print(prim(G,0))
