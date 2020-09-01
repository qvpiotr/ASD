#algorytm Floyda Warshalla

#dla grafów gestych, jezeli koszt z v do u wiekszy niz suma
#z v do k i z k do u to zamieniamy sumę na tę mniejszą


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

def floyd(G):

    D = [[0]*len(G) for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G)):
            if D[i][j]==0 and i!=j:
                D[i][j] = float("inf")

    for v in range(len(G)):
        for u in range(len(G)):
            if G[v][u]!=0:
                D[v][u]= G[v][u]

    for k in range(len(G)):
        for l in range(len(G)):
            for m in range(len(G)):
                D[l][m]=min(D[l][m], D[l][k]+D[k][m])

    return D

G = [[0,3,0,0,0,0,2,0,0],[3,0,2,1,0,0,0,0,0],[0,2,0,0,5,0,0,0,0],[0,1,0,0,1,7,0,0,0],[0,0,5,1,0,0,0,0,20],
[0,0,0,7,0,0,1,1,2],[2,0,0,0,0,1,0,3,0],[0,0,0,0,0,1,3,0,8],[0,0,0,0,20,2,0,7,0]]

#print(floyd(G))

print(max(max(floyd(G))))