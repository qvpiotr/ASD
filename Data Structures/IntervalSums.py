# Proszę zaimplementować klasę IntervalSums, która przechowuje tablicę n liczb (na pozycjach od 0 do n−1),
# pozwala zmieniać zadane liczby oraz obliczać sumę liczb na pozycjach od i do j.
# Państwa kod będzie uruchamiany. Proszę zaimplementować następujące funckcje w klase IntervalSums (można też dopisać inne klasy i/lub funkcje):
# 
# class IntervalSums:
#   def __init__(self, n):
#       # tworzy tablcę rozmiaru n, zainicjowaną zerami
#   def set( self, i, val ):
#       # zmienia zawartosc tablicy pod indeksem i na val
#   def interval( self, i, j ):
#       # zwraca sumę elementów tablice na pozycjach od i do j wlacznie
# 
# Przykładowe użycie klasy:
# IS = IntervalSums(4) # tworzy tablicę [0,0,0,0]
# IS.set(0,10) # [10,0,0,0]
# IS.set(2,-2) # [10,0,-2,0]
# IS.set(3,1) # [10,0,-2,1]
# IS.interval(0,3) # zwraca 10+0+(-2)+1 = 9
# IS.interval(1,2) # zwraca 0-2 = -2


class IntervalSums:
    def __init__(self, n):
        # tworzy tablcę rozmiaru n, zainicjowaną zerami
        self.n = n
        self.tab = [0]*n
    def set( self, i, val ):
        # zmienia zawartosc tablicy pod indeksem i na val
        self.tab[i] = val
    def interval( self, i, j ):
        # zwraca sumę elementów tablice na pozycjach od i do j wlacznie
        IntervalSums.build(self)
        return self.sum(0,i,j,0, (self.n)-1)

    def sum(self, v, i, j, l, r):
        if (i > j): return 0
        if i == l and j == r: return self.tree[v]
        m = (l+r)//2
        return self.sum( v*2+1, i, min(m,j), l, m ) + self.sum( v*2+2, max(m+1, i), j,m+1,r)

    def build(self):
        #buduje drzewo
        self.tree = [0] *(2*(self.n)-1)
        #liscie
        for i in range(self.n):
            self.tree[self.n+i-1] = self.tab[i]
        #rodzice
        a = 2*self.n-2
        while (a>=0):
            for i in range(a,a//2,-2):
                index = (i-1)//2
                self.tree[index] = self.tree[i]+self.tree[i-1]
            a = (a-1)//2
        
IS = IntervalSums(4) # tworzy tablicę [0,0,0,0]
IS.set(0,10) # [10,0,0,0]
IS.set(2,-2) # [10,0,-2,0]
IS.set(3,1) # [10,0,-2,1]
print(IS.interval(0,3)) # zwraca 10+0+(-2)+1 = 9
print(IS.interval(1,2)) # zwraca 0-2 = -2