class Node:
    def __init__(self, key, value, state):
        self.key = key
        self.value = value
        self.state = state

# state: 0 free 1 taken 2 keep looking

class Array:
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
        index = Array.hash(self, key)
        for _ in range (self.size):
            if self.array[index].state == 0 or self.array[index].state == 2:
                self.array[index].key = key
                self.array[index].value = value
                self.array[index].state = 1
                return
            index = (index + 1)%self.size


    # działa dla kluczy obecnych w tablicy rzeczywiscie (bez keep looking)
    def find(self, key):
        counter = 1
        index = Array.hash(self, key)
        for _ in range (self.size):
            if self.array[index].key == key and self.array[index].state == 1:
                return index % self.size, counter
            else: 
                index = (index + 1) % self.size
                counter += 1
    
    def display(self):
        for i in range(self.size):
            print(self.array[i].key, end = ' ')

def average(array):
    key_count = 0
    sum = 0
    table = []
    for i in range(array.size):
        if array.array[i].state == 1:
            key_count += 1
            table.append(array.array[i].key)
    for key in table:
        x,y = array.find(key)
        sum += y
    return sum/key_count



    
hashtable = Array(20)
Array.insert(hashtable, "Abra",1)
Array.insert(hashtable, "B",2)
#Array.insert(hashtable, "C",3)
#Array.insert(hashtable, "Labra",8)
Array.insert(hashtable, "Beka",4)
#Array.insert(hashtable, "Sraka",5)
#Array.insert(hashtable, "Gabson",6)
#Array.insert(hashtable, "Piterson",7)
Array.insert(hashtable, "Maria",9)
Array.insert(hashtable, "Mriaa",10)
Array.display(hashtable)
print(average(hashtable))
