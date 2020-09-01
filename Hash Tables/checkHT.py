class Node:
    def __init__(self, key, value, state):
        self.key = key
        self.value = value
        self.state = state

class HArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size
        for i in range(self.size):
            self.array[i] = Node(None, None, 0)

    def hash(self, key):
        v = int('0b10101010', 2)
        for l in key:
            v ^= ord(l) % 255
        return v % self.size

    def insert(self, key, value):
        index = HArray.hash(self, key)
        for _ in range (self.size):
            if self.array[index].state == 0 or self.array[index].state == 2:
                self.array[index].key = key
                self.array[index].value = value
                self.array[index].state = 1
                return
            index = (index + 1)%self.size

    def find(self, key):
        index = HArray.hash(self, key)
        for i in range (self.size):
            if self.array[index].key == key and self.array[index].state == 1: return index
            elif self.array[index].state == 0: return -1
            else: index = (index + 1) % self.size

    def display(self):
        for i in range(self.size):
            print(self.array[i].key, end = ' ')    

def checkHT(array):
    table = []
    for i in range (array.size):
        if array.array[i].state == 1:
            table.append((array.array[i].key,i))
    for key in table:
        if array.find(key[0]) != key[1]: return False
    return True 


hashtable = HArray(20)
HArray.insert(hashtable, "Abra",1)
HArray.insert(hashtable, "B",2)
#HArray.insert(hashtable, "C",3)
#HArray.insert(hashtable, "Labra",8)
HArray.insert(hashtable, "Beka",4)
#HArray.insert(hashtable, "Sraka",5)
#HArray.insert(hashtable, "Gabson",6)
#HArray.insert(hashtable, "Piterson",7)
HArray.insert(hashtable, "Maria",9)
HArray.insert(hashtable, "Mriaa",10)
HArray.display(hashtable)

print()

hashtable.array[13].state = 0
hashtable.array[2].state = 1
hashtable.array[2].key = "Maria"
hashtable.array[2].value = 9
HArray.display(hashtable)

print(checkHT(hashtable))