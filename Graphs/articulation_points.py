#DFS

#adjacency matrix representation



class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.entry = None
        self.low = None
        self.child = 0

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
                verticles[u].child += 1
                DFSVisit(v)  

                verticles[u].low = min(verticles[u].low, verticles[v].low)

                if verticles[u].parent is None and verticles[u].child > 1:
                    apoints.append(u)

                elif verticles[u].parent is not None and verticles[v].low >= verticles[u].entry:
                    apoints.append(u)

            elif verticles[v].visited and verticles[u].parent != v:
                verticles[u].low = min(verticles[u].low, verticles[v].entry)

        time +=1

        verticles[u].process = time

    apoints = []
    
    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    for v in range(len(G)):
        if verticles[v].visited == False:
            DFSVisit(v)
            
    
    
    return apoints


G = [[0,1,0,0,1], [1,0,1,1,1], [0,1,0,1,0], [0,1,1,0,0],[1,1,0,0,0]]
print(DFS(G))