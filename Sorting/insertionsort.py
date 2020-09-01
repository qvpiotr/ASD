def insertion_sort(tab):
    x = len(tab)-1
    for j in range(2,x,1):
        key = tab[j]
        i=j-1
        while i>0 and tab[i]>key:
            tab[i+1]=tab[i]
            i=i-1
        tab[i+1]=key

tablica = [23,33,2,1,232,33,45,71,2]

insertion_sort(tablica)
print(tablica)