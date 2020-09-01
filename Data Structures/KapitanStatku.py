# Kapitan pewnego statku zastanawia się, czy może wpłynąć do portu mimo tego, że nastąpił odpływ.
# Do dyspozycji ma mapę zatoki w postaci tablicy:
# int n = ...
# int m = ...
# int A[m][n];
# gdzie wartość A[y][x] to głębokość zatoki na pozycji (x,y). Jeśli jest ona większa niż pewna wartość
# int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0,0) a port znajduje się 
# na pozycji (n-1,m-1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio
# obok (tzn na pozycję, której dokładnie jedna współrzędna różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.

  
# struktura zbiorów rozłacznych

class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self    # na poczatku mamy zbiory jednoelementowe, wiec jako rodzic el. wskazuja samych siebie  
        self.rank=0         # wysokosc drzewa

# zwraca rerezentanta zbioru zawierajacego x
def find_set(x) :
    if x != x.parent :
        # rekurencyjnie "pniemy" sie w gore drzewa
        x.parent=find_set(x.parent)
        
    return x.parent # na samej gorze korzystamy z tego ze rodzic x to x


# łączy 2 zbiory w 1 (ten o mniejszej randze dołączamy do tego o większej)
def union(x,y):
    x=find_set(x)
    y=find_set(y)

    if x.rank > y.rank :
        y.parent=x
        
    elif y.rank > x.rank:
        x.parent=y

    else :
        x.parent=y
        y.rank+=1    # po złączeniu drzew o tych samych rozmiarach zwiększamy wysokość o 1




def isPossible(A,n,m,T):
    nodes = [[None]*n for _ in range (m)]
    for x in range(n):
        for y in range(m):
            nodes[x][y] = Node(A[x][y])
    
    for x in range(n):
        for y in range(m):
            if A[x][y] > T:
                if x-1 > 0 and A[x-1][y] > T: union(nodes[x-1][y], nodes[x][y])
                if x+1 < n and A[x+1][y] > T: union(nodes[x+1][y], nodes[x][y])
                if y-1 > 0 and A[x][y-1] > T: union(nodes[x][y-1], nodes[x][y])
                if y+1 < m and A[x][y+1] > T: union(nodes[x][y+1], nodes[x][y])

    return find_set(nodes[0][0]) == find_set(nodes[n-1][m-1])



A = [[8,9,7,5,3,2],[3,10,11,6,8,2],[2,12,9,5,9,3],[1,5,8,9,10,5],[2,3,3,5,6,6],[1,2,6,12,9,8]]
n = 6
m = 6
T = 7
print(isPossible(A,n,m,T))

