def search(tab):
  x = len(tab)
  if(x%2!=0): tab.append(tab[x-1])
  tmax = tab[0]
  tmin = tab[1]
  for i in range (0, x, +2):
    if(tab[i]>tab[i+1]):
      if(tab[i]>tmax): tmax = tab[i]
      if(tab[i+1]<tmin): tmin = tab[i+1]
    if(tab[i+1]>tmax): tmax = tab[i+1]
    if(tab[i]<tmin): tmin = tab[i]

  print("MAX to:", tmax,'\n',"MIN to:", tmin )

tablica = [1,12,13,2,33,45,23,100,22,0,-2,-13,37,-189]
search(tablica)



