# Zadanie 1. (problem sumy podzbioru) Dana jest tablica n liczb A. Prosze podac i zaimplementowac
# algorytm, który sprawdza, czy da sie wybrac podciag liczb z A, które sumuja sie do zadanej wartosci T.

def sum(A, T, suma, i):
    if suma == T: return True
    while i+1 < len(A):
        return sum(A, T, suma + A[i], i+1) or sum(A, T, suma, i+1)
    return False
    

A = [3,17,5,20,11,3,5,4,12,50,17]

print(sum(A, 70, 0, 0))
    