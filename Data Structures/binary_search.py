end = None


def wyszukiwanie_binarne(y):
    tablica = [0, 1, 2, 5, 12, 15, 23, 24, 45, 65, 66, 77, 78, 78, 78, 100]
    x = len(tablica)
    p = 0
    k = x - 1

    while p < k:
        srodek = (p + k) // 2
        if (p == srodek and tablica[p] != y and tablica[k] != y):
            return False
        if (tablica[srodek] == y):
            return True
        if (y < tablica[srodek]):
            k = srodek
        if (y > tablica[srodek]):
            p = srodek


end

result = wyszukiwanie_binarne(79)
if result:
    print("istnieje")
else:
    print("no nie")