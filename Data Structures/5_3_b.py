# Zadanie 3. (najdłuzszy podciag rosnacy) 
# 2. Na wykładzie podalismy algorytm działajacy w czasie O(n2). Prosze podac algorytm o złozonosci
# O(n log n).

def BSindex(A, l, r, key):
    while r > l + 1:
        m = l + (r-1) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r


def LIS(A):
    n = len(A)
    B = [0 for _ in range(n+1)]
    length = 0

    B[0] = A[0]
    length = 1
    for i in range(1, len(B)-1):
        if A[i] < B[i]:
            B[0] = A[i]
        elif A[i] > B[length-1]:
            B[length] = A[i]
            length += 1
        else:
            index = BSindex(A,-1, length -1, A[i])
            B[index] = A[i]
    return length
    


A = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(LIS(A))
