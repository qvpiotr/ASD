# Zadanie 3
# Zaproponuj strukturę danych udostępniającą następujący interfejs:

# init(length) - tworzy strukturę tablico-podobną o długości length.
# set(index, val) - podstawia pod index wartość val.
# snap() - tworzy snapa struktury i zwraca snap_id, identyfikujący aktualny 
#           snap - jest równy liczbie wykonanych do tej pory snapów.
# get(index, snap_id) - zwraca wartość jaka znajdowała się pod index wtedy 
#                   gdy wywołana funkcja snap zwróciła snap_id.

# Wszystkie operacje powinny być jak najszybsze!

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.right = None
        self.left = None

class BSTDict:

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        temp = self.root
        prev = None
        if self.root is None:
            self.root = Node(None, None)
            self.root.key = key
            self.root.value = value
            return
        while temp is not None:
            if temp.key < key:
                prev = temp
                temp = temp.right
            elif temp.key > key:
                prev = temp
                temp = temp.left
            else:
                temp.value = value
        if prev.key < key:
            prev.right = Node(None, None)
            prev.right.key = key
            prev.right.value = value
            prev.right.parent = prev
        else:
            prev.left = Node(None, None)
            prev.left.key = key
            prev.left.value = value
            prev.left.parent = prev
        return

    def find_key(self,key):
        temp = self.root
        while temp is not None:
            if temp.key == key:
                return temp
            elif temp.key > key:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def max(self, node):
        prev = None
        while node is not None:
            prev = node
            node = node.right
        return prev

class data:
    
    def __init__(self, length):
        # tablica drzew, poczatkowo root'y
        self.snap_id = 0
        self.array = [None]*length
        for i in range (length):
            self.array[i] = BSTDict()

    def set(self, index, val):
        # podstawia pod index wartość val.
        BSTDict.insert(self.array[index],self.snap_id,val)


    def snap(self):
        # tworzy snapa struktury i zwraca snap_id, identyfikujący aktualny 
        # snap - jest równy liczbie wykonanych do tej pory snapów.
        newarray = [None]* len(self.array)
        for i in range(len(self.array)):
            newarray[i] = data.get(self,i, self.snap_id)
        self.snap_id += 1
        return newarray


    
    def get(self, index, snap_id):
        n = snap_id
        node = Node(None, None)
        while n >= 0:
            node = BSTDict.find_key(self.array[index],n)
            if node is not None: break
            n-=1
        return node.value
        # zwraca wartość jaka znajdowała się pod index wtedy 
        # gdy wywołana funkcja snap zwróciła snap_id

tab = data(5)
tab.set(0,1)
tab.set(1,3)
tab.set(2,4)
tab.set(3,2)
tab.set(4,5)
for i in range (len(tab.array)):
    print(tab.snap()[i])
print('\n')
tab.set(0,2)
tab.set(1,3)
tab.set(2,4)
tab.set(3,3)
tab.set(4,1)
print(tab.get(1,0))
print(tab.get(1,1))
print(tab.get(4,0))