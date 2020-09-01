def knapsack(W, P, MaxW):
    n = len(W)
    F = [[0] * (MaxW+1) for _ in range (n)]
    for i in range (W[0], MaxW+1):
        F[0][i] = P[0]
    for i in range (n):
        for w in range (1, MaxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w - W[i]] + P[i])
    
    res = F[n-1][MaxW]
    temp = res
    items = []
    w = MaxW
    for i in range (n-1,-1,-1):
        if temp <= 0: break
        if temp == F[i][w]: continue
        else:
            items.append(i+1)
            w = w - W[i+1]
            temp = temp - P[i+1]
            i -= 1
        
    return res, items

W = [7,1,5,2,3,5,5,7]
P = [3,2,3,2,7,8,5,1]
MaxW = 12

print(knapsack(W,P, MaxW))