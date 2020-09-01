# Zadanie 4. (mnozenie macierzy) Dany jest cieg macierzy A1,A2, . . . ,An. Ktos chce policzyc iloczyn
# A1A2 · · ·An. Macierze nie sa koniecznie kwadratowe (ale oczywiscie znamy ich rozmiary). Zaleznie w jakiej
# kolejnosci wykonujemy mnozenia, koszt obliczeniowy moze byc rózny—nalezy podac algorytm znajdujacy
# koszt mnozenia przy optymalnym doborze kolejnosci.

def Matrix_Chain_Order(p):
    n = len(p)-1
    M = [[0] * (n+1) for i in range (n+1)]
    S = [[0] * (n+1) for i in range (n+1)]
    for l in range (2,n+1):
        for i in range (1, n+1-l+1):
            j = i + l -1
            M[i][j] = float('inf')
            for k in range (i, j):
                q = M[i][k] + M[k+1][j] + p[i-1]*p[k]*p[j]
                if q < M[i][j]:
                    M[i][j] = q
                    S[i][j] = k
                    
    def print_optimal(S,i,j):
        if j == i:
            print("{}{}".format("A",i), end='')
        else:
            print("(",end='')
            print_optimal(S,i,S[i][j])
            print_optimal(S, S[i][j]+1, j)
            print(")", end='')
    print_optimal(S,1,6)
    return M,S

p = [30,35,15,5,10,20,25]
Matrix_Chain_Order(p)