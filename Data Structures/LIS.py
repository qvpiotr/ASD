
def LIS(A):
    n = len(A)
    B = [1]*n
    P = [-1]*n
    for i in range (1,n):
        for j in range (i):
            if A[j] < A[i] and B[i] <= B[j]:
                B[i] =  B[j] + 1
                P[i] = j
    array = []
    def substring(A, P, i, array):
        if P[i]>=0:
            substring(A, P, P[i], array)
        array.append(A[i])
    
    substring(A, P, B.index(max(B)), array)
    
    return max(B), B, P, array




A = [3,1,5,7,2,4,9,3,17,3]
print(LIS(A))
