#algorytm Bellmana-Forda


class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.d = float("inf")
        

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]!=0:
            neigh.append(i)
    return neigh

def bellman(G,s):
    
    verticles = []
    for v in range (len(G)):
        verticles.append(vertex())
    verticles[s].d =0
    
    
    for _ in range (len(G)-1):
        for u in range (len(G)):
            for v in neighbour(G,u):
                if verticles[v].d > verticles[u].d + G[u][v]:
                    verticles[v].d = verticles[u].d + G[u][v]

                    verticles[v].parent = u
    
    for u in range(len(G)):
        for v in neighbour(G,u):
            if verticles[v].d > verticles[u].d + G[u][v]:
                print("False")
                return False


    return verticles

G = [[0,3,0,0,0,0,2,0,0],[3,0,2,1,0,0,0,0,0],[0,2,0,0,5,0,0,0,0],[0,1,0,0,1,7,0,0,0],[0,0,5,1,0,0,0,0,20],
[0,0,0,7,0,0,1,1,2],[2,0,0,0,0,1,0,3,0],[0,0,0,0,0,1,3,0,8],[0,0,0,0,20,2,0,7,0]]
Gr = [[0,5,0,0,0,0],[0,0,3,0,0,0],[0,0,0,2,0,0],[0,0,0,0,-15,6], [0,1,0,0,0,0],[0,0,0,0,0,0]]

bellman(Gr,0)