class Node:
    def __init__(self, key , value, state=0):
        self.key = -1
        self.value = value
        self.state = state # free, taken, deleted (0,1,2)

class HashArray:
    def __init__(self,size):
        self.size=size
        self.taken=0
        self.max_taken=0.8
        self.arr=[None]*self.size
        for i in range(size):
            self.arr[i]=Node(None,None)
    
    # latwo ustawiac i usuwac elementy
    # duzo pamieci
    # gdy n to liczba pierwsza daleka od potegi dwojki
    def hash1(self,key):
        return key%self.size

    def hash2(self,key):
        return 1+(key%(self.size-2))
    
    # pozycja w tablicy przy t-tym podejsciu
    # nie uzywamy dodatkowej pamieci
    # klasteryzajca
    # trudne usuwanie elementow
    def hash_otwarte_linowe(self,key,t):
        return (self.hash1(key)+t)%self.size


    def hash_podwojne(self,key,i):
        return (self.hash1(key)+i*self.hash2(key))%self.size


    def display(self):
        print("|", end = ' ')
        for i in range(self.size):
            if self.arr[i] is None: print(None)
            elif self.arr[i].state == 2: 
                print(self.arr[i].key,self.arr[i].value, "r", end = ' | ')
            else:
                print(self.arr[i].key,self.arr[i].value, end =" | ")

    def insert(self,klucz,value):
        if(self.taken==self.size):
            print("Wszystkie miejsca zajete")
            return
        i=0
        while i<self.size:
            j=HashArray.hash_otwarte_linowe(self,klucz,i)
            if self.arr[j].state==0 or self.arr[j].state==2:
                self.arr[j].value=value
                self.arr[j].key=klucz
                self.arr[j].state=1
                self.taken+=1
                return # insert na znalezionej wolnej pozycji
            elif self.arr[j].key==klucz:
                return
            i+=1
        # if self.taken/float(self.size)>= self.max_taken:
        #     self.resize()
    
    # def resize(self):
    #     self.size=self.size * 2
    #     self.taken=0
    #     prev_array=self.arr
    #     self.arr=[None]*self.size
    #     for i in range(size):
    #         self.arr[i]=Node(None,None)
    #     for node in prev_array:
    #         if node.key is not None:
    #             self

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

        
    
    def remove(self,klucz):
        i=1
        while i<self.size:
            j=HashArray.hash_otwarte_linowe(self,klucz,i)
            if(self.arr[j].key==klucz):
                self.arr[j].state=2
                return
            elif(self.arr[i].key!=klucz):
                i+=1
        return



def iscorrect(array, n):
    p = [0]*n
    last = 0
    for i in range (array.size):
        if array.arr[i%array.size].key == None:
            last = i
        p[i%array.size] = last%array.size
    
    for i in range (array.size):
        if array.arr[i].key != -1:
            j=HashArray.hash_otwarte_linowe(array,array.arr[i].key,0)
            if p[i] != p[j]: return False
    return True
        




array = HashArray(7)
array.insert(7,1)
array.insert(13,1)
array.insert(2,1)
array.insert(25,1)
array.insert(9,1)
array.arr[6].key = 2
array.arr[2].key = 13
array.display()
print(iscorrect(array,7))