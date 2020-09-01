#kolejka FIFO

class Node:
    def __init__(self):
        self.val = None
        self.next = None

class queue:

    def __init__(self):
        self.top = Node()
        self.top.next = None

    def enqueue(self, x):
        N = Node()
        N.val = x
        if queue.is_empty(kolejka):
            self.top.next = N
        else:
            last = self.top
            while last.next:
                last = last.next
            last.next = N

    def dequeue(self):
        N = self.top.next
        self.top.next = N.next
        return N.val

    def is_empty(self):
        return self.top.next == None

kolejka = queue()
queue.__init__(kolejka)
queue.enqueue(kolejka, 10)
queue.enqueue(kolejka, 17)
queue.enqueue(kolejka, 8)
queue.dequeue(kolejka)
queue.enqueue(kolejka, 9)
queue.enqueue(kolejka, 110)
queue.enqueue(kolejka, 10)
queue.dequeue(kolejka)
queue.dequeue(kolejka)
print(queue.is_empty(kolejka))







