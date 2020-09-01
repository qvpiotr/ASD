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
            node.right.right.parent = node
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

def inorder(root,array):
    if root is not None:
        inorder(root.left, array)
        array.append(root)
        inorder(root.right, array)
    
def merge(A,B):
    if len(A) == 0: return B
    elif len(B) == 0: return A
    array = []
    k = -1
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i].key<B[j].key:
            if k >= 0:
                if array[k].key != A[i].key: 
                    array.append(A[i])
                    i +=1
                    k +=1
                else: i +=1
            elif k == -1:
                array.append(A[i])
                k += 1
                i += 1
        elif A[i].key>B[j].key:
            if k >= 0:
                if array[k].key != B[j].key:
                    array.append(B[j])
                    j +=1
                    k +=1
                else: j += 1
            elif k == -1:
                array.append(B[j])
                k += 1
                j += 1
        else:
            i +=1
            j +=1
    if i == len(A) and j != len(B):
        while j < len(B):
            if array[k].key != B[j].key:
                array.append(B[j])
                j += 1
                k += 1
    if j == len(B) and i != len(A):
        while i < len(A):
            if array[k].key != A[i].key:
                array.append(A[i])
                i += 1
                k += 1
    return array

def twoBSTtoone(tree1, tree2):
    array1 = []
    array2 = []
    inorder(tree1.root, array1)
    inorder(tree2.root, array2)
    newarray = merge(array1, array2)
    tree = BSTDict()
    for node in newarray:
        BSTDict.insert(tree, node.key, node.value)
    return tree

################################################################################################

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

tree1 = BSTDict()
BSTDict.insert(tree1,53,1)
BSTDict.insert(tree1,30,2)
BSTDict.insert(tree1,27,3)
BSTDict.insert(tree1,40,4)
BSTDict.insert(tree1,63,5)
BSTDict.insert(tree1,75,6)
BSTDict.insert(tree1,120,6)
BSTDict.insert(tree1,80,6)
BSTDict.insert(tree1,93,6)
BSTDict.insert(tree1,110,6)

newtree = twoBSTtoone(tree1, tree)
BSTDict.display(newtree)



