# Zadanie 5. (wedrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Nalezy przejsc z pola (1, 1) na pole (n, n) korzystajac jedynie z ruchów “w dół”
# oraz “w prawo”. Wejscie na dane pole kosztuje tyle, co znajdujaca sie tam liczba. Prosze podac algorytm
# znajdujacy trase o minimalnym koszcie.

def chessboard(A):
    n = len(A)
    M = [[0]*n for i in range (n)]
    for i in range (1,n):
        M[0][i] = M[0][i-1] + A[0][i]
        M[i][0] = M[i-1][0] + A[i][0]
    for i in range (1,n):
        for j in range (1,n):
            M[i][j] = min(M[i-1][j]+A[i][j], M[i][j-1]+A[i][j])

    return M[n-1][n-1]

A = [[3,5,2,3,4],[2,1,11,2,3],[4,5,2,3,3],[2,2,4,5,6],[1,22,4,5,6]]
print(chessboard(A))