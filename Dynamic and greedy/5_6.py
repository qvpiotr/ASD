# Zadanie 6. (wydawanie monet) Mamy dana tablice z nominałami monet stosowanych w pewnym dziwnym
# kraju, oraz kwote T. Prosze podac algorytm, który oblicza minimalna ilosc monet potrzebna do wydania
# kwoty T (algorytm zachłanny, wydajacy najpierw najwieksza monete, nie działa: dla monet 1, 5, 8 wyda
# kwote 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).

def coins(r,C):
    n = len(C)
    O = [[0]*r for i in range (n)] 
    for i in range (n):
        for j in range(r):
            if i == 0: O[i][j] = j+1
            elif j+1 == C[i]: O[i][j] = 1
            elif j<C[i] and j>1: O[i][j] = O[i-1][j]
            else: O[i][j] = min(O[i][j-C[i]]+1, O[i-1][j])


    array = []
    i = n-1
    j = r-1
    var = r
    while O[i][j] == O[i-1][j]: i -= 1
    index = i
    temp = C[index]
    while var > 0:
        var -= temp
        if var>=0: array.append(C[index])
        else: var += temp
        if var < temp:
            index -= 1
            temp = C[index]

    return O[n-1][r-1], array

C = [1,2,5,7,9]
print(coins(13,C))