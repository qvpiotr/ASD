from random import randint
import math
# n no liczba kubelkow jakie tworzymy, musimy znac ja chociazby przyblizona

def bucketSort(arr, a):
    n = 11
    Max = max(arr)
    buckets = [[] for _ in range(n)] 
    
    for i in arr:
        # normalizacja: dzielimy elementy przez max, dzieki czemu wszystkie beda z przedzialu [0,1]
        normNum = i/Max 
        bucketIdx = int((n-1) * normNum) # wybieram bucket
        buckets[bucketIdx].append(i)     # dodaje liczbe do bucketa
    
    for i in range(n):
        buckets[i] = sorted(buckets[i], key = log(x,a))     
        #sortuje obojetnie jaka metoda, bo liczba elementow jest stala
    
    output = []
    
    for i in range(n): # i-ty bucket
        for j in range(len(buckets[i])): # j-ty element
            output.append(buckets[i][j])
    return output,buckets
