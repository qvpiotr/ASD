

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
path = 0
maxpath = 0
def DFS(G):


    def DFSVisit(u):
        global time
        global path
        global maxpath
        time+=1
        
        
        verticles[u].visited = True
        verticles[u].entry = time
        for v in neighbour(G, u):
            if verticles[v].visited == False and verticles[v].d <=2:
                verticles[v].parent = u
                path += 1
                DFSVisit(v)
        if path > maxpath: maxpath = path        
        time +=1
        verticles[u].process = time

    
    verticles = []
    for i in range (len(G)):
        verticles.append(vertex())
        verticles[i].d = len(neighbour(G,i))
    for v in range(len(G)):
        # path = 0
        if verticles[v].visited == False and verticles[v].d <=2:
            DFSVisit(v)
            

    return maxpath

G = [[0,1,0,0,0,1],[1,0,1,0,0,0],[0,1,0,1,1,0],[0,0,1,0,1,0],[0,0,1,1,0,1],[1,0,0,0,1,0]]
DFS(G)
print(maxpath)