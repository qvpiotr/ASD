# Dana jest struktura struct HT{ int* table; int size; }, która opisuje tablicę haszującą
# rozmiaru size, przechowującą liczby nieujemne. Tablica korzysta z funkcji haszującej int
# hash(int x) i liniowego rozwiązywania konfliktów (ujemne wartości w tablicy table oznaczają
# wolne pola). Doskonałością takiej tablicy nazywamy liczbę elementów x takich, że pozycja x w
# tablicy to hash(x) mod size (a więc x jest na ”swojej” pozycji). Proszę napisać funkcję:
# void enlarge( HT* ht);
# która powiększa tablicę dwukrotnie i wpisuje elementy w takiej kolejności, by doskonałość
# powstałej tablicy była jak największa. Funkcja powinna być możliwie jak najszybsza.

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
        return key % self.size

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

def enlarge(hash_table):
    size = hash_table.size
    new_hash_table = HArray(2*size)

    for node in hash_table.array:
        if node.state == 1:
            index = HArray.hash(new_hash_table, node.key)
            if new_hash_table.array[index].state == 0:
                HArray.insert(new_hash_table, node.key, node.value)
                node.state = 0
    for node in hash_table.array:
        if node.state == 1:
            HArray.insert(new_hash_table, node.key, node.value)

    return new_hash_table




hashtable = HArray(14)
HArray.insert(hashtable, 56,56)
HArray.insert(hashtable, 16,16)
HArray.insert(hashtable, 44,44)
HArray.insert(hashtable, 5,5)
HArray.insert(hashtable, 19,19)
HArray.insert(hashtable, 36,36)
HArray.insert(hashtable, 78,78)
HArray.insert(hashtable, 79,79)
HArray.insert(hashtable, 11,11)
HArray.insert(hashtable, 81,81)
HArray.display(hashtable)
print()

HArray.display(enlarge(hashtable))


