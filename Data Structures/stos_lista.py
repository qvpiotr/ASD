#stos implementacja listowa


class Node:
    def __init_(self):
        self.next = None
        self.val = None

class Stack:
    def __init__(self):
        self.top = Node()  # wartownik
        self.top.next = None

    def push(self, x):
        N = Node()
        N.val = x
        N.next = self.top.next
        self.top.next = N

    def pop(self):
        N = self.top.next
        self.top.next = N.next
        return N.val

    def is_empty(self):
        return self.top.next == None


stos = Stack()
Stack.__init__(stos)
Stack.push(stos,10)
Stack.push(stos,9)
Stack.pop(stos)
Stack.push(stos,8)
Stack.push(stos,7)
Stack.pop(stos)
Stack.push(stos,6)
Stack.push(stos,5)
Stack.pop(stos)
print(Stack.is_empty(stos))





