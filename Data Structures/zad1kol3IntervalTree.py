

from inttree import *
from operator import itemgetter

# przykladowy test uzycia drzewa przedzialowego 
# T = tree([1, 2, 3, 4, 5])
# tree_insert(T,(1, 4))
# tree_insert(T,(2, 5))
# tree_print(T)
# tree_remove(T,(1, 4))
# print()
# tree_print(T)
# tree_insert(T,(1, 3))
# print(tree_intersect(T, 3))
# exit(0)



def intervals( I ):
    max_d = max(I)[1]
    min_d = min(I)[0]
    array = []
    for i in range(min_d, max_d+1):
        array.append(i)
    # nie wszytskie naturalne z przedzialu
    T = tree(array)
    
    result = []
    d = 0

    for i in range(len(I)):
        tree_insert(T, I[i])
        interval_array = tree_intersect(T,I[i][1]) + tree_intersect(T,I[i][0]) 
        minimum = min(interval_array, key = itemgetter(0))[0]
        maximum = max(interval_array, key = itemgetter(1))[1]
        tree_insert(T,(minimum,maximum))
        tree_remove(T, I[i])
        d = max(d,maximum-minimum)
        result.append(d)
    

    return result






# uruchamia bazowe testy uzywajac funkcji intervals do obliczania wyniku
#wypisuje na koncu "OK!" jesli testy zaliczone
run_tests(intervals)






