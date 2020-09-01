'''
    Dana jest formuła logiczna w postaci 2CNF. To znaczy, że formuła jest koniunkcją klauzuli,
    gdzie każda klauzula to alternatywa dwóch literałów, a każdy literał to zmienna lub jej negacja.
    Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest: (x ∨ y) ∧ ( ~x ∨ z ) ∧ ( ~z ∨ ~y).
    Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartościowanie spełniające formułę.
'''

# 2-SAT is a special case of Boolean Satisfiability Problem and can be solved in polynomial time.


# ALGORYTM:

'''
    Zauważmy, że każdą alternatywę dwóch literałów można przedstawić jako dwie implikacje, np:
    (x v y) = ( ~x => y ) ∧ (~y => x), ponieważ jeżeli jeden jest fałszywy, to na pewno drugi musi
    byc prawdziwy, by cała klauzula była prawdziwa.
    Możemy więc całą daną formułę przedstawić jako graf implikacji, w którym dla każdej klauzuli 
    mamy dwie krawędzi.
    Wiemy też, że:
        (x => y) = (y => x),
        jeżeli (x => ~x), to wiemy, że x=0
        jeżeli (~x => x), to wiemy, że x=1
        więc jeżeli w grafie istnieją dwie powyższe krawędzi, to nie ma wartościowania spełniającego
        formułę, ponieważ x musiałoby jednocześnie być prawdziwe i fałszywe
        jeżeli (x => y) ∧ (y => z), to wiemy, że (x => z), czyli mając ścieżkę w grafie, jest to
        równoznaczne z tym, że mogłaby istnieć taka bezpośrednia krawędź
        jeżeli w jednej silnie spójnej składowej jest x i ~x, to False, ponieważ z def. SSC (Strongly
        Connected Component) jeżeli 2 wierzchołki są w jednej, to istnieje ściezka w obie strony, co nie
        może mieć miejsca (opisano wyżej).
    -----------------------------------------------------------------------------------------------------------
    Żeby nie dopuścić do sprzeczności  przy wartościowaniu (może być tak że x jest osiągalny z ~x i odwrotnie,
    lecz NIE JEDNOCZEŚNIE), należy posortować topologicznie silnie spójne składowe,
    wtedy jeżeli SCC z x jest przed SCC z ~x, to x=0, analogicznie odwrotnie.
'''

# po prostu SCC i sprawdzamy, czy zmienna i jej zaprzeczenie nie należą do tej samej składowej
# '+' implies 'OR'
# '-' implies 'AND'
# (x1+x2)*(x2’+x3)*(x1’+x2’)*(x3+x4)*(x3’+x5)*(x4’+x5’)*(x3’+x4)
# a = [1,-2,-1,3,-3,-4,-3]
# b = [2,3,-2,4,5,-5,4]
# n - number of variables

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
    
    result = []
    

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

    def DFSVisitTime(u,array):
        verticles[u].visited = True
        array.append(u)
        for v in neighbourREV(G, u):
            if verticles[v].visited == False:
                verticles[v].parent = u
                DFSVisitTime(v,array)

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
            array = []
            DFSVisitTime(ver,array)
            if len(array) > 1:
                result.append(array)
            maxprocess = 0
    
    return result
        
def is2Satisfiable(a,b,n):
    G = [[0]*2*n for _ in range(2*n)]
    for i in range(len(a)):
        if a[i] < 0:
            temp1 = abs(a[i]) + n
            positive1 = False
        elif a[i] > 0:
            temp1 = a[i]
            positive1 = True
        if b[i] < 0:
            temp2 = abs(b[i]) + n
            positive2 = False
        elif b[i] > 0:
            temp2 = b[i]
            positive2 = True
        if positive1 is True:
            posx = temp1
            negx = posx + n
        elif positive1 is False:
            posx = temp1 #posx = temp1 - n
            negx = temp1 - n #negx = temp1
        if positive2 is True:
            posy = temp2
            negy = temp2 + n
        elif positive2 is False:
            posy = temp2 # posy = temp2 - n
            negy = temp2 - n # negy = temp2
        
        G[negx-1][posy-1] = 1
        G[posy-1][negx-1] = -1
        G[negy-1][posx-1] = 1
        G[posx-1][negy-1] = -1
    print(G)
    array = SSS(G)
    if len(array) == 0: return False
    print(array)
    for i in range(len(array)):
        array1 = [0]*2*n
        for j in range(len(array[i])):
            x = array[i][j]
            array1[x] += 1
            if x+n < 2*n:
                if array1[x+n] == array1[x]: return False
            else:
                if array1[x-n] == array1[x]: return False
    return True


a = [1,-2,-1,3,-3,-4,-3]
b = [2,3,-2,4,5,-5,4]
n = 5
print(is2Satisfiable(a,b,n))

c = [1, -1, 1, -1]
d = [2, 2, -2, -2]
m = 2
print(is2Satisfiable(c,d,m))