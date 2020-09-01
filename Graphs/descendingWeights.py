
class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.entry = 0
        self.process = 0

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i] != 0:
            neigh.append(i)
    return neigh

time = 0
temp = 0
def DFS(G, S, X):
    
    def DFSVisit(u):
        global time
        global temp
        time+=1
        verticles[u].visited = True
        verticles[u].entry = time
        if u == S:
            for v in neighbour(G, u):
                if verticles[v].visited == False:
                    verticles[v].parent = u
                    temp = G[u][v] 
                    DFSVisit(v)
        elif u is not S:
            for v in neighbour(G, u):
                if verticles[v].visited == False and G[u][v] < temp:
                    verticles[v].parent = u
                    temp = G[u][v] 
                    DFSVisit(v)            

        time +=1
        verticles[u].process = time

    
    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    DFSVisit(S)

    return verticles[X].visited


G = [[0]*6 for i in range (6)]
G[0][1] = 13
G[1][0] = 13
G[1][2] = 10
G[2][1] = 10
G[2][3] = 8
G[3][2] = 8
G[3][4] = 6
G[4][3] = 6
# G[3][5] = 11
# G[5][3] = 11
G[5][4] = 3
G[4][5] = 3
G[2][4] = 9
G[4][2] = 9
G[4][3] = 6
G[3][4] = 6
G[0][4] = 17
G[4][0] = 17




print(DFS(G,1,5))

print(DFS(G,5,3))