def partition(tab,p,r):
    x = tab[r]
    i = p-1
    for j in range (p,r,1):
        if tab[j]<=x:
            i=i+1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[r]=tab[r],tab[i+1]
    return i+1


def quicksort(tab,p,r):
    if p<r:
        q=partition(tab,p,r)
        quicksort(tab,p,q-1)
        quicksort(tab,q+1,r)

#funkcja spr
tablica = [213,22,4,33,222,55342,21,11,8,44,1]
quicksort(tablica, 0, len(tablica)-1)
print(tablica)
