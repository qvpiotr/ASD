# Zadanie 2
# Opisz, jak zmodyfikować drzewa czerwono czarne tak, aby
# można było w czasie O(log(n)) wyznaczyć sumę wszystkich 
# elementów w drzewie o wartościach z zakresu (x, y). W wyniku 
# wykonanej modyfikacji pozostałe operacje na drzewie również 
# powinny zachować swoją pierwotną złożoność.Oczywiście należy 
# również opisać jak będzie przebiegała operacja obliczania sumy.

# W węźle należy trzymać sumę liczb w prawym i lewym poddrzewie. Teraz operacja: znajdujemy wspólnego roota 
# dla węzłów o wartościach x oraz y (jest to pierwszy węzeł, z którego idziemy w inne strony szukając węzła x i y).
# Aby znaleźć poszukiwaną sumę, trzeba przejść od węzła x rekurencyjnie w górę. Dla samego węzła x bierzemy sumę 
# jego prawego poddrzewa. Gdy idziemy wyżej, to mogliśmy przyjść albo z lewego dziecka, albo z prawego dziecka:
# 1) gdy przyszliśmy z lewego dziecka, to przyszliśmy z elementu mniejszego - dodajemy sumę prawego poddrzewa, 
# elementu z aktualnego węzła i idziemy wyżej
# 2) gdy przyszliśmy z  prawego dziecka, to przyszliśmy z elementu 
# wniejszego - po prostu idziemy wyżej Przerywamy operację, gdy dojdziemy do naszego wspólnego roota. 

# Dla y wykonujemy analogiczną operację, ale w lustrzanym odbiciu - gdy przyszliśmy z lewego dziecka, 
# to po prostu idziemy wyżej, a gdy przyszliśmy z prawego dziecka, to dodajemy sumę lewego poddrzewa 
# (z mniejszymi elementami), element z aktualnego węzła i idziemy wyżej.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        self.suml = key
        self.sumr = key

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
            self.root.sumr = 0
            self.root.suml = 0
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
            prev.right.sumr = 0
            prev.right.suml = 0
            current = prev.right
            while prev is not None:
                if prev.right is not None and prev.right == current :
                    prev.sumr += key
                else:
                    prev.suml += key
                current = prev
                prev = prev.parent
        else:
            prev.left = Node(None, None)
            prev.left.key = key
            prev.left.value = value
            prev.left.parent = prev
            prev.left.sumr = 0
            prev.left.suml = 0
            current = prev.left
            while prev is not None:
                if prev.left is not None and prev.left == current:
                    prev.suml += key
                else:
                    prev.sumr += key
                current = prev
                prev = prev.parent
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

def sum(root, x, y):
    node = root
    sum = 0
    #znajduje węzeł wspólny dla przedzialu (x,y)
    while node is not None:
        if node.key >= x and node.key <= y: break
        if node.key < x: node = node.right
        elif node.key > y: node = node.left
    sum += node.key
    lnode = node
    lprev = lnode
    while lnode is not None:
        if lnode.key == x: break
        elif lnode.key < x:
            lprev = lnode
            lnode = lnode.right
        else:
            lprev = lnode
            lnode = lnode.left
        if lnode is None:
            lnode = lprev.parent
            break  
    rnode = node
    rprev = rnode
    while rnode is not None:
        if rnode.key ==y: break
        elif rnode.key < y:
            rprev = rnode
            rnode = rnode.right
        else:
            rprev = rnode
            rnode = rnode.left
        if rnode is None:
            rnode = rprev
            break
    
    # sum += lnode.sumr + lnode.key
    while lnode != node:
        if lnode == lnode.parent.left and lnode.key >= x:
            sum += lnode.sumr
            sum += lnode.key 
        elif lnode == lnode.parent.right:
            sum += lnode.key
            sum += lnode.sumr
        lnode = lnode.parent

    while rnode != node:
        if rnode == rnode.parent.right and rnode.key <= y:
            sum += rnode.suml
            sum += rnode.key
        elif rnode == rnode.parent.left:
            sum += rnode.suml
            sum += rnode.key
        rnode = rnode.parent
    
    return sum

            
    

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

#tworze drzewo czerwono czarne, przechowując w kazdym węźle
#sumę prawego i lewego poddrzewa + wartosc wezla
newtree = BSTDict()
newtree = toRB(tree.root)
BSTDict.display(newtree)
print(sum(newtree.root, 30, 80))






