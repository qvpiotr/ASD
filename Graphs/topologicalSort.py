#adjacency matrix representation

#A - graph, S - start vertex

class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.entry = 0
        self.process = 0

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]==1:
            neigh.append(i)
    return neigh

time = 0
def TS(G):
    
    array = [None]*len(G)
    def DFSVisit(u):
        global time
        global i
        time+=1
        verticles[u].visited = True
        verticles[u].entry = time
        for v in neighbour(G, u):
            if verticles[v].visited == False:
                verticles[v].parent = u
                DFSVisit(v)  
        time +=1
        verticles[u].process = time
        array[i]=u
        i-=1

    
    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    for v in range(len(G)):
        if verticles[v].visited == False:
            DFSVisit(v)
    return array

G = [[0,1,0,0,1,1], [0,0,1,0,1,0], [0,0,0,1,0,0], [0,0,0,0,0,0],[0,0,0,0,0,0], [0,0,0,0,0,0]]
i = len(G)-1
print(TS(G))