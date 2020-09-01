#algorytm Kruskala
# O(ElogV)
#1.Posortowac krawedzie rosnaca wg wag
#2.Pusty zbior krawedzi MST
#3.dla kazdego v make_set(v)
#4.dla kazdej krawedzi u,v jesli naleza do innych zbiorów
#  union(u,v) 

class Node:
    def __init__(self,id):
        self.id = id
        self.parent = self
        self.rank = 0

def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank +=1

class vertex:
    def __init__(self):
        self.visited = False
        self.d = 0
        self.parent = None

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]!=0:
            neigh.append(i)
    return neigh

def kruskal(G):
    edges = []
    for u in range(len(G)):
        for v in neighbour(G,u):
            if not (G[u][v],u,v) in edges:
                edges.append((G[u][v],v,u))
    edges = sorted(edges)

    sum = 0

    MST = []
    sets = []

    for i in range(len(G)):
        sets.append(Node(i))
    
    for e in edges:
        if find_set(sets[e[1]]) != find_set(sets[e[2]]):
            MST.append(e)
            sum += e[0]
            union(sets[e[1]],sets[e[2]])

    return MST,sum
    

G = [[0,2,0,1,6,0,0],[2,0,3,0,0,0,0],[0,3,0,2,0,0,1],
[1,0,2,0,0,5,0],[6,0,0,0,0,8,0],[0,0,0,5,8,0,7],[0,0,1,0,0,7,0]]

print(kruskal(G))
