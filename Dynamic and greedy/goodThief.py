#kolokwium 3 2016/17
#zad2

def goodThief(arr):
    n = len(arr)

    stolen = [False]*n
    dp = [0]*n

    #w tablicy dp wartosc i-tego elementu to max wartosc 
    #dla przedmiotów od 0 do i wlacznie

    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])

    for i in range(2,n):
        dp[i]=max(dp[i-1], dp[i-2]+arr[i])

    for i in range(n-1, 1, -1):
        if dp[i]==dp[i-2]+arr[i] and (i==n-1 or stolen[i+1] is False):
            stolen[i] = True
    
    if stolen[2] is True: stolen[0] is True
    else:
        if arr[0]>arr[1]: stolen[0]=True
        else: stolen[1]=True

    for i in range(n):
        if stolen[i] : print(i)

    return dp[n-1]