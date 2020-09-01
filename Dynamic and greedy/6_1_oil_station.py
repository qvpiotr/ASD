# Zadanie 1. (problem stacji benzynowych) Pewien podróznik chce przebyc trase z punktu A do punktu
# B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy (mozna powiedziec, ze
# jedzie czołgiem... znaczenie punktów A i B w ramach obecnej sytuacji geopolitycznej wybierzcie sobie sami).
# W baku miesci sie dokładnie D litrów paliwa. Trasa z A do B to prosta, na której znajduja sie stacje
# benzynowe. Mamy dwa rózne zadania (rozwiazywane osobno):
# (1) wyznaczyc trase, na której tankujemy minimalna liczbe razy.
# (2) wyznaczyc trase, której koszt jest minimalny (wówczas znamy jeszcze dla kazdej stacji cene za litr
# paliwa, nie musimy zawsze tankowac do pełna).
# (3) Bonus: j.w., ale jesli na stacji tankujemy, to musimy zatankowac do pełna.

def station1(A,D):
    result = 0
    # A[0] = A = 0   A[len(A)-1] = B = x kilometrów
    n = len(A)-1
    pos = A[1]
    i = 1
    L = D - pos
    while pos != A[n] and i < n+1:
        if L >= A[i+1] - pos:
            L = L - A[i+1] + pos
            pos = A[i+1]
            i += 1
        else:
            result += 1
            L = D
            continue
    return result

A = [0,30,40,45,80,100,120,150,185]
print(station1(A, 40))

def station2(A,D):
    cost = 0
    n = len(A)
    pos = A[0][0]
    L = D
    # trasa krótsza niż zasięg
    if A[n-1][0] <= D: return 0
    # szukam pierwszej najtanszej stacji w zasiegu D
    i = 1
    spos = 0
    sprice = float ('inf')
    while A[i][0] <= D and i < n-1:
        if A[i][1]<sprice:
            sprice = A[i][1]
            spos = i
        i += 1
    L -= A[spos][0]
    j = spos + 1
    while j <= n-1 and A[j][0] <= D:
        


B = [[0,0],[10,3],[40,4],[54,3]]
print(station2(B,50))




