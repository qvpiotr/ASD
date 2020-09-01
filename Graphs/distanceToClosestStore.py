
from queue import PriorityQueue

class vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.d = float("inf")
        

def neighbour(G,s):
    neigh = []
    for i in range (len(G)):
        if G[s][i]>0:
            neigh.append(i)
    return neigh

def dijkstry(array,s):
    q = PriorityQueue()

    verticles = []
    for v in range (len(array)):
        verticles.append(vertex())
    verticles[s].d =0

    for v in range (len(array)):
        q.put((float("inf"), v))
    
    while not q.empty():
        u = q.get()
        for v in array[u[1]].edges:
            if verticles[v].d > verticles[u[1]].d + array[u[1]].distances[array[u[1]].edges.index(v)]:
                verticles[v].d = verticles[u[1]].d + array[u[1]].distances[array[u[1]].edges.index(v)]
                q.put((verticles[v].d, v))

                verticles[v].parent = u[1]
    
    return verticles

class VertexInTown:
    def __init__(self, shop, distances, edges):
        self.shop = shop #true-shop false-house
        self.distances = distances #tablica odleglosci do innych wierzchołków
        self.edges = edges #numery wierzchołków opisanych w distances
        self.edge = len(self.edges)
        self.d_store = [] #odleglosc do najblizszego sklepu




A = VertexInTown(False, [7,22], [3,6])
B = VertexInTown(True, [18,2,7,7,0], [2,3,4,5,8])
C = VertexInTown(True, [18,0],[1,8])
D = VertexInTown(False, [2,7,20],[1,0,5])
E = VertexInTown(True, [7,6,0],[1,5,8])
F = VertexInTown(False, [7,20,6,15], [1,3,4,7])
G = VertexInTown(False, [22,20],[0,7])
H = VertexInTown(False, [15,20],[5,6])
I = VertexInTown(False, [0,0,0],[1,2,4])
array = [A,B,C,D,E,F,G,H,I]


def distanceToClosestStore(array):
    for ver in array:
        if ver.shop == True: ver.d_store = 0
        else: ver.d_store = dijkstry(array,array.index(ver))[len(array)-1].d


distanceToClosestStore(array)
for ver in array:
    print(ver.d_store)

