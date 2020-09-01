
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
def DFS(G, S, X, P, T):
    
    def DFSVisit(u):
        global time
        time+=1
        verticles[u].visited = True
        verticles[u].entry = time
        for v in neighbour(G, u):
            if abs(G[u][v] - P) <= T: 
                if verticles[v].visited == False:
                    verticles[v].parent = u
                    DFSVisit(v)  
        time +=1
        verticles[u].process = time

    
    verticles = []
    for _ in range (len(G)):
        verticles.append(vertex())
    DFSVisit(S)
    return verticles[X].visited


def Bajtocja(G,X,Y,T):
    for v in neighbour(G,X):
        P = G[X][v]
        for i in range (P-T, P+T):
            if DFS(G,X,Y,i,T) is True: return True
    return False

G = [[0]*6 for i in range (6)]
G[0][4] = 19
G[4][0] = 19
G[0][3] = 26
G[3][0] = 26
G[1][4] = 22
G[4][1] = 22
G[1][2] = 18
G[2][1] = 18
G[2][3] = 23
G[3][2] = 23
G[5][2] = 25
G[2][5] = 25
G[4][5] = 21
G[5][4] = 21

print(Bajtocja(G,1,5,2))
print(Bajtocja(G,1,0,1))