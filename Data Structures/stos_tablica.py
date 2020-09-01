#stos implementacja tablicowa


class Stack:
    def __init__(self, n):
        self.S = [None]*n
        self.n = n
        self.elements = 0

    def push(self, x):
        self.S[self.elements] = x
        self.elements += 1

    def pop(self):
        self.elements -= 1
        return self.S[self.elements]

    def is_empty(self):
        return self.elements == 0


stos = Stack(10)
Stack.__init__(stos, 10)
for i in range (10):
    Stack.push(stos, i)
Stack.pop(stos)
Stack.pop(stos)
Stack.pop(stos)
x = Stack.is_empty(stos)
print(x)


