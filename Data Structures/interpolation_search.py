def interpolation_search(tab,val):
  p = 0
  k = len(tab) -1
  while (tab[p]<=val and tab[k]>=val):
    i = p +((val-tab[p])*(k-p)//(tab[k]-tab[p]))
    if(tab[i]==val): return True
    if(tab[i]<val): p = i+1;
    if(tab[i]>val): k = i-1;
  return False

tablica = [11, 23, 24, 24, 25, 26, 26, 33, 105, 111, 123, 234, 255, 456, 543, 654, 2233, 12333]
if(interpolation_search(tablica,24)): print("istnieje")
else: print("nie istnieje")






