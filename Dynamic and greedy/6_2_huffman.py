# Zadanie 2 (kody Huffmana)
# Dana jest tablica n liczb naturalnych A. Liczba A[i] mówi ile razy i-ty symbol
# pojawia sie w tekscie. Prosze zaimplementowac funkcje huffman len(A), która
# oblicza ile bitów zajełoby zapisanie tekstu składajacego sie własnie z takiej liczby
# symboli, jesli uzytoby optymalnego kodu Huffmana. Funkcja powinna działac
# w czasie O(n log n). Podpowiedz: Moze sie przydac struktura kopca.
# Panstwa kod powinien miec nastepujaca postac (bedzie uruchamiany; prosze nie
# usuwac fragmentu testujacego; sprawdzajacy moze takze dołozyc swoje testy):
# def huffman_len(A):
# # tu prosze umiescic swoja implementacje
# # elementarny test, powinien wypisac 2600
# print( huffman_len([ 200, 700, 180, 120, 70, 30] )

#HEAP
class Heap():

    def __init__(self,A):
        self.heaplist=A
        self.heapsize = len(A)

    def left(self, i):
        if i==0: return 2
        else: return 2*i

    def right(self, i):
        if i==0: return 3
        else: return 2*i+1

    def parent(self, i):
        return 2//i


    def max_heapify(self,i):
        if i == 0: tmp = 0
        else: tmp = i-1
        l = self.left(i)-1
        r = self.right(i)-1
        if(l<self.heapsize and self.heaplist[tmp]<self.heaplist[l]):
            largest = l
        else:
            largest = tmp
        if(r<self.heapsize and self.heaplist[r]>self.heaplist[largest]):
            largest = r
        if largest != tmp:
            self.heaplist[largest], self.heaplist[tmp] = self.heaplist[tmp], self.heaplist[largest]
            self.max_heapify(largest+1)

    def min_heapify(self,i):
        if i == 0: tmp = 0
        else: tmp = i-1
        l = self.left(i)-1
        r = self.right(i)-1
        if(l<self.heapsize and self.heaplist[tmp]>self.heaplist[l]):
            smallest = l
        else:
            smallest = tmp
        if(r<self.heapsize and self.heaplist[r]<self.heaplist[smallest]):
            smallest = r
        if smallest != tmp:
            self.heaplist[smallest], self.heaplist[tmp] = self.heaplist[tmp], self.heaplist[smallest]
            self.min_heapify(smallest + 1)

    def built_max(self):
        for i in range (self.heapsize//2, 0 ,-1):
            self.max_heapify(i)

    def built_min(self):
        for i in range(self.heapsize//2, 0, -1):
            self.min_heapify(i)

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.level = 0


def huffman_len(A):
    heap = Heap(A)
    heap.built_min()
    B = []
    
    while heap.heapsize > 1:
        temp1 = heap.heaplist[0]
        if heap.heapsize > 2:
            temp2 = min(heap.heaplist[1], heap.heaplist[2])
        else:
            temp2 = heap.heaplist[1]
        node1 = Node(temp1)
        node2 = Node(temp2)
        node12 = Node(temp1+temp2)
        B.append(node1)
        B.append(node2)
        B.append(node12)
        heap.heaplist.append(temp1+temp2)
        heap.heaplist.remove(temp1)
        heap.heaplist.remove(temp2)
        heap.heapsize = len(heap.heaplist)
        heap.built_min()

    root = Node(None)
    tmp = root
    i = len(B)-1
    tmp = B[i]
    while i >= 2:
        tmp.right = B[i-1]
        tmp.left = B[i-2]
        tmp.right.parent = tmp
        tmp.left.parent = tmp
        tmp.right.level = tmp.level + 1
        tmp.left.level = tmp.level + 1
        if i == 2: break
        if i == (len(B)-1): root = tmp 
        if i-3 > 0:
            if B[i-3].val == tmp.left.val:
                i -= 3
                tmp = tmp.left
            elif B[i-3].val == tmp.right.val:
                i -= 3
                tmp = tmp.right 
            else:
                i -= 3
                tmp = tmp.parent.left
        
    result = 0
    for i in range (len(B)-1):
        if B[i].left is None and B[i].right is None:
            result += B[i].level * B[i].val  
            

    return result

def display_tree(root):

    def print_tree(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.val
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = print_tree(root.left)
                s = '%s' % root.val
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = print_tree(root.right)
                s = '%s' % root.val
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = print_tree(root.left)
            right, m, q, y = print_tree(root.right)
            s = '%s' % root.val
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
        
    print()
    lines, _, _, _ = print_tree(root)
    for line in lines:
        print(line)
    print()



    

A = [700,200,180,120,70,30]

print(huffman_len(A))


