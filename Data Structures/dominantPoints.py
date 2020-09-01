# Punkt 1 dominuje nad 2 gdy x1>x2 i y1>y2. Podaj liczność najmnijeszego zbioru
# punktów, które dominują nad wszystkimi pozostałymi

class point:
    def __init__(self,val1,val2):
        self.x = val1
        self.y = val2

import operator

def maxset(A):
    result = 0
    A.sort(key = operator.itemgetter(0))
    B = sorted(A, key = operator.itemgetter(1))
    B.reverse()
    A.reverse()
    print(A)
    print(B)
    for i in range (len(A)):
        if A[i] == B[i]: result += 1
        else: break
    return result

A = [(2,8),(1,3),(4,5),(7,8),(9,10),(2,11),(19,20),(8,5),(4,2),(3,12),(11,5)]
B = [(4,2),(2,4),(3,3),(1,1),(0,1)]

print(maxset(B))