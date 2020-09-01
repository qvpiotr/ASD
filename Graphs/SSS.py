#SSS

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

def neighbourREV(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]==-1:
            neigh.append(i)
    return neigh

time = 0
def SSS(G):
    
    def DFSVisit(u):
        global time
        time+=1
        verticles[u].visited = True
        verticles[u].entry = time
        for v in neighbour(G, u):
            if verticles[v].visited == False:
                verticles[v].parent = u
                DFSVisit(v)  
        time +=1
        verticles[u].process = time

    def DFSVisitTime(u):
        verticles[u].visited = True
        print(u, end=' ')
        for v in neighbourREV(G, u):
            if verticles[v].visited == False:
                verticles[v].parent = u
                DFSVisitTime(v)

    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    for v in range(len(G)):
        if verticles[v].visited == False:
            DFSVisit(v)

    for v in verticles:
        v.visited = False
    
    maxprocess = verticles[0].process
    ver = 0
    
    for i in range (len(G)):
        for v in range(len(verticles)):
            if verticles[v].process > maxprocess and verticles[v].visited == False:
                maxprocess = verticles[v].process
                ver = v
        if verticles[i].visited == False:
            DFSVisitTime(ver)
            print('')
            maxprocess = 0
        
        

G = [[0,1,-1,0,1,0,0,0,0,1,0], [-1,0,1,0,0,0,0,0,0,0,0], [1,-1,0,1,0,0,0,0,0,0,0], [0,0,-1,0,-1,1,0,0,0,0,0],
    [0,0,0,1,0,-1,1,0,0,0,0], [0,0,0,-1,1,0,-1,0,0,0,-1], [0,0,0,0,-1,1,0,-1,0,0,0], [0,0,0,0,0,0,1,0,-1,1,0],
    [0,0,0,0,0,0,0,1,0,0,-1], [-1,0,0,0,0,0,0,-1,0,0,1], [0,0,0,0,0,1,0,0,1,-1,0]]
SSS(G)

G1 = [[0,1,-1,0,1,0,0,0,0,1,0], [-1,0,1,0,0,0,0,0,0,0,0], [1,-1,0,0,1,0,0,0,0,0,0], [0,0,0,0,-1,1,0,0,0,0,0],
    [0,0,-1,1,0,-1,1,0,0,0,0], [0,0,0,-1,1,0,-1,0,0,0,-1], [0,0,0,0,-1,1,0,-1,0,0,0], [0,0,0,0,0,0,1,0,-1,1,0],
    [0,0,0,0,0,0,0,1,0,0,-1], [-1,0,0,0,0,0,0,-1,0,0,1], [0,0,0,0,0,1,0,0,1,-1,0]]
SSS(G1)

G2=[[0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, -1, 0, 1, 1, 0, 0, 0, -1, 0], [0, 0, -1, 0, 0, 0, 0, -1, 0, 1], [0, 0, -1, 0, 0, 0, 0, 0, 1, 0], [0, -1, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0, -1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, -1, -1], [0, 0, 1, 0, -1, 0, 0, 1, 0, 0], [0, 0, 0, -1, 0, 0, 0, 1, 0, 0]]
SSS(G2)