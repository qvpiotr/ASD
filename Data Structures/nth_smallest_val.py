import random

def partition(tab, p, r):
    x=tab[r]
    i = p-1
    for j in range (p, r, 1):
        if tab[j]<=x:
            i=i+1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[r]=tab[r],tab[i+1]
    return i+1

def rand_partition(tab, p, r):
    s = random.randint(p,r)
    tab[s],tab[r]=tab[r],tab[s]
    return partition(tab,p,r)

def rand_select(tab, p, r, i):
    #przypadek bazowy rekursji tablica jednoelementowa
    if p==r: return tab[p]
    #dzielimy tablice na dwie
    q = rand_partition(tab,p,r)
    #obliczamy ilosc elementow w tablicy dolnej plus element rozdzielający
    k = q-p+1
    if i==k: return tab[q]
    elif i<k: return rand_select(tab, p, q-1, i)
    else: return rand_select(tab, q+1, r, i-k)

tablica = [1, 2, 3, 2, 5, 6, 4, 55, 332, 122, 2, 3, -2]
x = rand_select(tablica, 0,12,7)
print (x)