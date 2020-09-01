#DFS

#adjacency matrix representation

#A - graph, S - start vertex

class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.entry = 0
        self.process = 0
        self.d = 0

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]==1:
            neigh.append(i)
    return neigh

time = 0
def Diameter(G, S):
    
    def DFSVisit(u):
        global time
        time+=1
        verticles[u].visited = True
        verticles[u].entry = time
        if u is not S:
            verticles[u].d = verticles[verticles[u].parent].d + 1
        for v in neighbour(G, u):
            if verticles[v].visited == False:
                verticles[v].parent = u
                DFSVisit(v)  
        time +=1
        verticles[u].process = time

    
    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    DFSVisit(S)

    array = []
    for i in verticles:
        array.append(i.d)
    max_d = max(array)
    id = array.index(max_d)
    

    for v in verticles:
        v.visited = False
        v.parent = None
        v.entry = 0
        v.process = 0
        v.d = 0
    S = id
    DFSVisit(id)
    for v in verticles:
        array[verticles.index(v)] = v.d
    return max(array)
        

G = [[0,1,0,0,1,0,1,0,0], [1,0,1,0,0,0,0,0,0], [0,1,0,1,0,0,0,0,0], [0,0,1,0,0,0,0,0,0],
[1,0,0,0,0,1,0,1,0], [0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,1],[0,0,0,0,0,0,0,1,0]]
print(Diameter(G,0))