# Zadanie 2. (najdłuzszy wspólny podciag) Mamy dane dwie tablice, A[n] i B[n]. Nalezy znalezc długosc
# ich najdłuzszego wspólnego podciagu. (Klasyczny algorytm dynamiczny O(n2)).

def longest_substring(A, B):
    n = len(A)
    x = [[0]*(n+1) for _ in range(n+1)]
    y = [[None]*(n+1) for _ in range(n+1)]
    for i in range (1,n+1):
        for j in range (1, n+1):
            if A[i-1] == B[j-1]:
                x[i][j] = x[i-1][j-1]+1
                y[i][j] = "ok"
            elif x[i-1][j] >= x[i][j-1]:
                x[i][j] = x[i-1][j]
                y[i][j] = "|"
            else:
                x[i][j] = x[i][j-1]
                y[i][j] = "<-"
    
    i = j = n
    array = []
    while y[i][j] is not None:
        if y[i][j] == 'ok':
            array.append(B[j-1])
            i -= 1
            j -= 1
        elif y[i][j] == "|":
            i-=1
        else:
            j-=1
    array.reverse()
            
            

    return x[n][n], array

A = [3,4,5,2,1,4]
B = [3,0,4,5,5,1]
print(longest_substring(A,B))

    