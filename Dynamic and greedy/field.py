#kolokwium3 15/16
#zad 2

#w dp dp[i] oznacza maksymalna osiagalna wartosc z
# pola itego do konca. Idziemy od konca tablicy i dla kolejnych
# pol decydujemy, czy lepiej skoczyc o long czy short
# szukana wartosc to dp[0]

class field:
    def __init__(self,value,short,long):
        self.value=value
        self.short=short
        self.long=long

def max_val(arr):
    n = len(arr)
    dp=[0]*len(arr)
    dp[n-1]=arr[n-1].value

    for i in range(n-2,-1,-1):
        dp[i]=dp[i+arr[i].short]+arr[i].value
        if i+arr[i].long<n:
            dp[i]=max(dp[i], dp[i+arr[i].long]+arr[i].value)
            
    return dp[0]