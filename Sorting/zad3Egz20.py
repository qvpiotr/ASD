from zad3testy import runtests
import math

    
def fast_sort(arr, a):
    n = 11
    buckets = [[] for _ in range(n)] 
    
    for i in arr:
        bucketIdx = math.floor(math.log(i,2)/len(arr)) 
        buckets[bucketIdx].append(i)    
    
    for i in range(n):
        buckets[i] = sorted(buckets[i])     
        #sortuje obojetnie jaka metoda, bo liczba elementow jest stala
        #nie wbudowanym
    
    output = []
        
    for bucket in buckets:
        output += bucket
    return output

    



runtests( fast_sort )
