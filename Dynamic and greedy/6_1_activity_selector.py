# Zadanie 1 (wybór zajec)
# Dana jest n elementowa tablica A = [(b1, e1), . . . , (bn, en)], gdzie kazda para
# (bi, ei) oznacza zajecia rozpoczynajace sie w chwili bi i konczace w chwili ei.
# Prosze zaimplementowac funkcje tasks(A), która zwraca ile maksymalnie zajec
# mozna wybrac tak, by na siebie nie nachodziły. Mozna załozyc, ze wszystkie
# liczby w tablicy A sa naturalne. Przedziały nalezy traktowac jako otwarte, czyli
# np. zajecia (1, 3) oraz (3, 5) nie nachodza na siebie.

import operator

def tasks(A):
    n = len(A)
    A.sort(key = operator.itemgetter(1))
    result = 1
    k = A[0][1]
    for i in range (1,n):
        if A[i][0] >= k:
            result += 1
            k = A[i][1]
    return result  



A = [(3,5),(1,4),(2,3),(3,7),(4,5),(5,7),(8,9),(3,11)]
print(tasks(A))
print(tasks([ (0,10), (10,20), (5,15) ]))