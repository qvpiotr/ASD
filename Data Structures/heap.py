#HEAP

class Heap():

    def __init__(self):
        self.heaplist=[0]
        self.heapsize = 0

    def left(self, i):
        if i==0: return 2;
        else: return 2*i

    def right(self, i):
        if i==0: return 3;
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
            self.max_heapify(smallest + 1)

    def built_max(self):
        for i in range (self.heapsize//2, 0 ,-1):
            self.max_heapify(i)

    def built_min(self):
        for i in range(self.heapsize//2, 0, -1):
            self.min_heapify(i)

def heapsort(A):
    kopiec = Heap()
    Heap.__init__(kopiec)
    kopiec.heaplist = A
    kopiec.heapsize = len(A)
    kopiec.built_max()

    for i in range(kopiec.heapsize, 1, -1):
        A[0],A[kopiec.heapsize-1]=A[kopiec.heapsize-1],A[0]
        kopiec.heapsize -= 1
        kopiec.max_heapify(0)

#sprawdzanie

A = [13,22,12,12,5,3,2,10]
print(A)
#heapsort(A)
#print(A)
kopiec1 = Heap()
Heap.__init__(kopiec1)
kopiec1.heaplist=A
kopiec1.heapsize=8
kopiec1.built_min()
print(kopiec1.heaplist)



