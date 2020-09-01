class Cyclist:
    def __init__(self, id, id_p):
        self.id = id
        self.id_p = id_p

class BetterCyclist:
    def __init__(self, id, id_p, id_n):
        self.id = id
        self.id_p = id_p
        self.id_n = id_n

class HArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size
        for i in range(self.size):
            self.array[i] = BetterCyclist(-1, -1, -1)

    def hash(self, key):
        return key%self.size

    def insert(self, cyclist):
        index = HArray.hash(self, cyclist.id)
        for _ in range (self.size):
            if self.array[index].id == -1:
                self.array[index].id = cyclist.id
                self.array[index].id_p = cyclist.id_p
                return 
            else: index = (index + 1) % self.size

    def find(self, key):
        index = HArray.hash(self, key)
        for _ in range (self.size):
            if self.array[index].id == key: return index
            else: index = (index + 1) % self.size
        return None

def smallestGroup(cyclist_array):
    hashtable = HArray(2*len(cyclist_array))
    for cyclist in cyclist_array:
        HArray.insert(hashtable, cyclist)

    for i in range (hashtable.size):
        if hashtable.array[i].id != -1 and hashtable.array[i].id_p != -1:
            index = HArray.find(hashtable, hashtable.array[i].id_p)
            hashtable.array[index].id_n = hashtable.array[i].id
        
    smallest = float('inf')
    size = 1

    for better_cyclist in hashtable.array:
        if better_cyclist.id != -1 and better_cyclist.id_n == -1:
            current = better_cyclist
            while(hashtable.array[HArray.find(hashtable,current.id_p)].id_p != -1):
                size += 1
                current = hashtable.array[HArray.find(hashtable,current.id_p)]
            size += 1
            if size < smallest:
                smallest = size
                size = 1

    return smallest


cyclist1=Cyclist(5,-1)
cyclist2=Cyclist(2,1)
cyclist3=Cyclist(7,5)
cyclist4=Cyclist(13,2)
cyclist5=Cyclist(8,7)
cyclist6=Cyclist(19,8)
cyclist7 = Cyclist(1,6)
cyclist8 = Cyclist(6,10)
cyclist9 = Cyclist(10,-1)


tab=(cyclist1, cyclist2, cyclist3, cyclist4, cyclist5, cyclist6, cyclist7, cyclist8, cyclist9)
print(smallestGroup(tab))