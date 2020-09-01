# Zadanie 4
# Zaproponuj strukturę danych udostępniającą następujący interfejs:
# init(capacity) - inicjalizuje strukturę na pojemność capacity.
# get(key) - zwraca wartość pod kluczem key, lub -1 jeśli klucza 
#            nie ma (struktura przechowuje liczby naturalne).
# put(key, val) - wkłada pod klucz key wartość val.

# Jeżeli w wyniku operacji put liczba kluczy mogłaby przekroczyć capacity, 
# to należy usunąć klucz na którym najrzadziej wykonywano operację get. 
# Jeżeli istnieje kilka takich kluczy, to należy usunąć ten, na którym 
# ostatnia wykonana operacja get była najwcześniejsza.
# Wszystkie operacje powinny być jak najszybsze!

##############################################################################

# Jest to problem LFU cache (Least Frequently Used).
# Wersja mniej ambitna - O(log(n)):
# Wartości pod kluczami trzymamy w zwykłym słowniku. Dodatkowo mamy jeszcze drzewo,
# gdzie kluczami są częstotliwości (liczby wykonanych get’ów), a wartościami listy 
# kluczy ze słownika. Wykonując get wyciągamy klucz z listy pod odpowiednią częstotliwością 
# w drzewie i dopinamy go na koniec listy pod częstotliwością o 1 większą. Ewentualne usuwanie 
# przy put, to po prostu usunięcie pierwszego elementu z listy pod najmniejszym kluczem w drzewie. 
# Żeby wszystko działało szybko, to w słowniku pod danym kluczem trzeba jeszcze trzymać częstotliwość, 
# oraz wskazanie na węzeł listy. Warto dodać, że na kolosie słownik trzymając klucze powinien być drzewem,
# ponieważ nie zmienia to rzędu złożoności operacji, a pozwala uchronić się przed ćwiczeniowcami z ciemnogrodu.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.frequency = 0
        self.parent = None
        self.right = None
        self.left = None

class BSTDict:

    def __init__(self):
        self.root = None
    
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

    def min(self, node):
        prev = None
        while node is not None:
            prev = node
            node = node.left
        return prev

    def max(self, node):
        prev = None
        while node is not None:
            prev = node
            node = node.right
        return prev

    def successor(self, key):
        node = BSTDict.find_key(self, key)

        if node is None: return None

        #minimalny element z prawego poddrzewa
        if node.right is not None:
            return BSTDict.min(self, node.right)

        #nie istnieje prawe poddrzewo

        while node.parent is not None and node.parent.left != node:
            node = node.parent

        return node.parent
            

    def predecessor(self, key):
        node = BSTDict.find_key(self, key)

        if node is None: return None

        #maksymalny element z lewego poddrzewa
        elif node.left is not None:
            return BSTDict.max(self, node.left)

        #nie istnieje lewe poddrzewo

        while node.parent is not None and node.parent.right != node:
            node = node.parent
        return node.parent

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
                return
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


    def remove(self, key):
        node = BSTDict.find_key(self, key)
        if node is None: return
        
        #node to be deleted is leaf
        if node.left is None and node.right is None:
            #leaf is left child
            if node.parent.left == node:
                node.parent.left = None
            #leaf is right child
            elif node.parent.right == node:
                node.parent.right = None

        #node to be deleted has only one child
        #left
        elif node.left is not None and node.right is None:         
    
            new_key = node.left.key
            new_value = node.left.value
            new_right = node.left.right
            new_left = node.left.left
            node.left.left.parent = node
            node.left.right.parent = node    
            node.key = new_key
            node.value = new_value
            node.left = new_left
            node.right = new_right
        #right
        elif node.left is None and node.right is not None:
            
            new_key = node.right.key
            new_value = node.right.value
            new_right = node.right.right
            new_left = node.right.left
            if node.right.right is not None:
                node.right.right.parent = node
            if node.right.left is not None:
                node.right.left.parent = node
            node.key = new_key
            node.value = new_value
            node.left = new_left
            node.right = new_right
            
        
        #node to be deleted has two children
        else:
            tmp = BSTDict.successor(self, node.key)
            new_value = tmp.value
            new_key = tmp.key
            BSTDict.remove(self, tmp.key)
            node.value = new_value
            node.key = new_key

    def display(self):

        def _display_aux(self):
        #Returns list of strings, width, height and horizontal coordinate of the root

        #no child
            if self.right is None and self.left is None:
                line = '%s' % self.key
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle
            
        #only left child
            if self.right is None:
                lines, n, p ,x = _display_aux(self.left)
                s = '%s' % self.key
                u = len(s)
                first_line = (x+1) * ' ' + (n-x-1) * '_' + s
                second_line = x * ' ' + '/' + (n-x-1+u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n+u, p+2, n+u //2

        #only right child
            if self.left is None:
                lines, n, p ,x = _display_aux(self.right)
                s = '%s' % self.key
                u = len(s)
                first_line = s + x * '_' + (n-x) * ' '
                second_line = (u+x) * ' ' + '\\' + (n-x-1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u //2

        #two children
            left, n, p, x = _display_aux(self.left)
            right, m, q, y = _display_aux(self.right)
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2


        lines, _, _, _ = _display_aux(self.root)
        for line in lines:
            print(line)
            
####################################################            


class lfu:

    def __init__(self, capacity):
        self.counter = 0
        self.capa = capacity
        self.dict = BSTDict()
        self.freq = BSTDict()
        BSTDict.insert(self.freq, 0, None)
        node = BSTDict.find_key(self.freq, 0)
        node.value = []
        

    def get(self, key):
        result = BSTDict.find_key(self.dict, key)
        if result is None: return -1
        node = BSTDict.find_key(self.freq, result.frequency)
        node.value.remove(key)
        if len(node.value) == 0: BSTDict.remove(self.freq, result.frequency)
        result.frequency += 1
        node = BSTDict.find_key(self.freq, result.frequency)
        if node is None:
            BSTDict.insert(self.freq, result.frequency, None)
            node1 = BSTDict.find_key(self.freq, result.frequency)
            node1.value = []
            node1.value.append(key)
        else:
            node.value.append(key)
        return result.value

    def put(self, key, value):
        if self.dict.root is None:
            BSTDict.insert(self.dict, key, value)
            self.counter += 1
            node = BSTDict.find_key(self.freq, 0)
            node.value.append(key)
            return
        elif BSTDict.find_key(self.dict, key) is not None:
            BSTDict.insert(self.dict, key, value)
            return
        elif BSTDict.find_key(self.dict, key) is None and self.counter < self.capa:
            BSTDict.insert(self.dict, key, value)
            self.counter += 1
            node = BSTDict.find_key(self.freq, 0)
            node.value.append(key)
        else:
            #musimy usunac pierwszy na liscie pod najmniejszym kluczem w freq
            minimum = BSTDict.min(self.freq, self.freq.root).key
            node = BSTDict.find_key(self.freq, minimum)
            key_to_delete = node.value[0]
            node.value.pop(0)
            BSTDict.remove(self.dict, key_to_delete)
            BSTDict.insert(self.dict, key, value)
            node1 = BSTDict.find_key(self.freq, 0)
            node1.value.append(key)





str = lfu(6)
lfu.__init__(str,6)
str.put(40,400)
str.put(10,100)
str.put(50,500)
str.put(30,300)
str.put(20,200)
str.put(60,600)
str.put(70,700)

str.put(30,333)
print(str.get(30))


BSTDict.display(str.dict)
BSTDict.display(str.freq)
print(str.freq.root.value)


