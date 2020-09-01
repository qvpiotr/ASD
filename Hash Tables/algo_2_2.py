# Zadanie 2.
# Dany jest zbiór n punktów na płaszczyźnie dwuwymiarowej, w postaci tablicy par liczb. 
# Podaj jak najszybszy algorytm zwracający rozmiar największego podzbioru tych punktów, 
# takiego, że wszystkie są współliniowe.

# Dla każdej pary punktów obliczamy parametry prostej na której leżą. Wstawiamy taką parę 
# (a, b) do słownika i inkrementujemy tam licznik.

class Node:
    def __init__(self, prosta):
        self.prosta = prosta
        self.counter = 0

class HashArray:
    def __init__(self,size):
        self.size=size
        self.taken=0
        self.max_taken=0.8
        self.arr=[None]*self.size
        for i in range(size):
            self.arr[i]=Node(None)
    
    def hash3(self,tuple):
        return ( tuple[1] << 16 ) ** tuple[0]

    def display(self):
        print("|", end = ' ')
        for i in range(self.size):
            if self.arr[i] is None: print(None)
            elif self.arr[i].state == 2: 
                print(self.arr[i].key,self.arr[i].value, "r", end = ' | ')
            else:
                print(self.arr[i].key,self.arr[i].value, end =" | ")

    def insert(self,tupla):
        i=0
        while i<self.size:
            j=HashArray.hash3(tupla)%self.size
            if self.arr[j].counter==0:
                self.arr[j].prosta=tupla
                self.arr[j].counter+=1
                return # insert na znalezionej wolnej pozycji
            elif self.arr[j].counter>0:
                self.arr[j].counter+=1
                return
            i+=1


    def find(self,klucz):
        i=1
        while i<self.size:
            j=HashArray.hash_otwarte_linowe(self,klucz,i)
            if(self.arr[j].key==klucz):
                return self.arr[j].value
            elif(self.arr[j].key!=klucz and self.arr[j].state!=0):
                i+=1
            elif(self.arr[j].key!=klucz and self.arr[j].state==0):
                return


def parametry(tab):
    l=len(tab)
    array=HashArray(l*l)
    for i in range (l):
        for j in range(l):
            if(tab[i][0]!=tab[j][0] and tab[i][1]!=tab[j][1]):
                if(tab[i][0]-tab[j][0])!=0 and (tab[i][1]-tab[j][1])!=0:
                    a=(float(tab[i][1]-tab[j][1]))/float((tab[i][0]-tab[j][0]))
                    b=tab[i][1]-a*tab[i][0]
                    punkt=(a,b)
                    array.insert(punkt)
                elif(tab[i][0]-tab[j][0])==0:
                    a=tab[i][0]
                    b=float("inf")
                elif(tab[i][1]-tab[j][1])==0:
                    a=0
                    b=tab[i][1]

    max=0
    while i < array.size:
        if array.arr[i].counter>max:
            max=array.arr[i].counter
        i+=1
    return max
        
    


tab=[(5,6),(7,8),(2,4),(9,10)]
parametry(tab)