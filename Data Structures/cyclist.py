class Cyclist:
    def __init__(self, id, przed):
        self.id = id
        self.przed = przed

class BetterCyclist:
    def __init__(self, id, przed):
        self.id = -1
        self.za = -1
        self.przed = None

class HashArray:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*self.size
        for i in range(size):
            self.arr[i]=BetterCyclist(-1,None)
    

    def hash1(self,key):
        return key%self.size

    def hash_otwarte_linowe(self,key,t):
        return (self.hash1(key)+t)%self.size


    def display(self):
        print("|", end = ' ')
        for i in range(self.size):
            if self.arr[i] is None: print(None)
            elif self.arr[i].id == -1: 
                print(self.arr[i].za,self.arr[i].id,self.arr[i].przed,  end = ' | ')
            else:
                print(self.arr[i].za,self.arr[i].id,self.arr[i].przed, end =" | ")

    def insert(self,cyclist):
        i=0
        while i<self.size:
            j=HashArray.hash_otwarte_linowe(self,cyclist.id,i)
            if self.arr[j].id == -1:
                self.arr[j].id=cyclist.id
                self.arr[j].przed=cyclist.przed
                return # insert na znalezionej wolnej pozycji
            elif self.arr[j].id==id:
                return
            i+=1
    

    def find(self,key):
        i=0
        while i<self.size:
            if key is None: return None
            j=HashArray.hash_otwarte_linowe(self,key,i)
            if(self.arr[j].id==key):
                return self.arr[j] 
            i+=1



def smallest(array):

    hash_array = HashArray(2*len(array))

    for i in range(len(array)):
        node = BetterCyclist(-1, None)
        node.id = array[i].id
        node.za = -1
        node.przed = array[i].przed
        hash_array.insert(node)

    for i in range (len(array)):
        current = array[i]
        if current.przed == -1: continue
        nastepnik = hash_array.find(current.przed)
        nastepnik.za = current.id 

    minimum = len(array)
    size = 0
    for i in range (2*len(array)):
        if hash_array.arr[i].id != -1 and hash_array.arr[i].za == -1:
            current = hash_array.arr[i]
            while hash_array.find(current.przed) != -1 and hash_array.find(current.przed) is not None:
                size += 1
                current = hash_array.find(current.przed)
            if size < minimum:
                minimum = size
            size = 0

    return minimum

    
    
    # for i in range(size):
    #     cur=array.arr[i]
    #     if cur.id!=None:
    #         new_array.insert(cur)

    # for i in range(size):
    #     cur=array.arr[i]
    #     if cur.przed!=-1 and cur.id!=None:
    #         new_array.find(cur)
    






cyclist1=Cyclist(5,-1)
cyclist2=Cyclist(2,1)
cyclist3=Cyclist(7,5)
cyclist4=Cyclist(13,2)
cyclist5=Cyclist(8,7)
cyclist6=Cyclist(19,8)
cyclist7 = Cyclist(1,-1)


tab=(cyclist1, cyclist2, cyclist3, cyclist4, cyclist5, cyclist6, cyclist7)
print(smallest(tab))