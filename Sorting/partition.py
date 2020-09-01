def partition(tab, p, r):
    x=tab[r]
    i = p-1
    for j in range (p, r, 1):
        if tab[j]<=x:
            i=i+1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[r]=tab[r],tab[i+1]
    return i+1
