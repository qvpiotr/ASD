# Zadanie 1
# Podaj algorytm, który mając na wejściu niezrównoważone drzewo BST 
# przekształca je w drzewa dające się pokolorować jako czerwono-czarne.

# Wpisujemy do tablicy zawartość drzewa, w porządku inorder. Otrzymujemy 
# posortowaną tablicę. Teraz mamy rekurencyjną funkcję, która tworzy BST. 
# Bierzemy medianę z tablicy, robimy z niej korzeń i teraz rekurencyjne 
# wywołanie na lewo i prawo od mediany. Otrzymane drzewo jest idealnie 
# zrównoważone, więc na pewno jest i RB i AVL.

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



def inorder(root,array):
    if root is not None:
        inorder(root.left, array)
        array.append(root)
        inorder(root.right, array)
    


def toRB(root):
    newtree = BSTDict()
    array = []
    inorder(root, array)
    rek(root, newtree, array, 0, len(array)-1)
    BSTDict.insert(newtree, array[len(array)-1].key, array[len(array)-1].value)
    return newtree


def rek(root, newroot, array, r, l):
    while(r != l):
        mediana = (l+r)//2
        BSTDict.insert(newroot, array[mediana].key, array[mediana].value)
        rek(root, newroot, array,r, mediana)
        rek(root, newroot, array,mediana+1, l)
        return

    
    
tree = BSTDict()
BSTDict.insert(tree,50,1)
BSTDict.insert(tree,30,2)
BSTDict.insert(tree,20,3)
BSTDict.insert(tree,40,4)
BSTDict.insert(tree,60,5)
BSTDict.insert(tree,70,6)
BSTDict.insert(tree,100,6)
BSTDict.insert(tree,80,6)
BSTDict.insert(tree,90,6)
BSTDict.insert(tree,110,6)

BSTDict.display(tree)
print('\n')
BSTDict.display(toRB(tree.root))


