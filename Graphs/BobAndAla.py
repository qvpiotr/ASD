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

def dijkstry(G,s,y,person):
    q = PriorityQueue()

    verticles = []
    for v in range (len(G)):
        verticles.append(vertex())
    verticles[s].d =0

    for v in range (len(G)):
        q.put((float("inf"), v, person))
    
    per = person
    while not q.empty():
        u = q.get()
        for v in neighbour(G,u[1]):
            if u[2] == 'Ala':
                temp = G[u[1]][v]
                per = 'Bob'
            elif u[2] == 'Bob':
                temp = 0
                per = 'Ala'
            if verticles[v].d > verticles[u[1]].d + temp:
                verticles[v].d = verticles[u[1]].d + temp
                q.put((verticles[v].d, v, per))

                verticles[v].parent = u[1]
    
    array = []
    v = y
    while v is not s:
        array.insert(0,v)
        v = verticles[v].parent
    array.insert(0,s)

    return person, verticles[y].d, array


def BobAndAla(G,x,y):
    result1 = dijkstry(G,x,y,'Ala')
    result2 = dijkstry(G,x,y,'Bob')
    if result1[1] > result2[1]:
        return result2
    else: return result1

####################################################
G = [[0]*7 for i in range (7)]
G[0][1] = 5
G[1][0] = 5
G[1][2] = 12
G[2][1] = 12
G[1][6] = 7
G[6][1] = 7
G[6][3] = 4
G[3][6] = 4
G[3][2] = 3
G[2][3] = 3
G[3][4] = 6
G[4][3] = 6
G[5][4] = 25
G[4][5] = 25
G[5][3] = 8
G[3][5] = 8

print(BobAndAla(G,5,0))

