#DFS

#adjacency matrix representation
#find bridges


class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.entry = None
        self.low = None

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]==1:
            neigh.append(i)
    return neigh

time = 0

time = 0
def DFS(G):
    
    def DFSVisit(u):
        global time
        time+=1
        verticles[u].visited = True
        verticles[u].entry = time
        verticles[u].low = time
        for v in neighbour(G, u):
            if verticles[v].visited == False:
                verticles[v].parent = u
                DFSVisit(v)  

                verticles[u].low = min(verticles[u].low, verticles[v].low)

            elif verticles[v].visited and verticles[u].parent != v:
                verticles[u].low = min(verticles[u].low, verticles[v].entry)

        time +=1
        verticles[u].process = time

    
    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    for v in range(len(G)):
        if verticles[v].visited == False:
            DFSVisit(v)
            
    bridges = []
    for v in range (len(verticles)):
        if verticles[v].entry == verticles[v].low and verticles[v].parent is not None:
            bridges.append([verticles[v].parent, v])

    return bridges


G = [[0,1,0,1,0,0,0], [1,0,1,0,0,0,0], [0,1,0,1,1,0,0], [1,0,1,0,0,0,0], [0,0,1,0,0,1,1],[0,0,0,0,1,0,1], [0,0,0,0,1,1,0]]
print(DFS(G))