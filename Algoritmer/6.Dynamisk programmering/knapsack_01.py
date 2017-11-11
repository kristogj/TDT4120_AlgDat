

weights = [2,5,10]
values = [3,15,20]

#n = number of objects to choose from
#W = max weight
#Eksponensiell kjøretid
def knapsack01(n,W):
    if n == -1: #Siden jeg bruker 0-indeksering må n være -1 for å ikke peke på en gjenstand
        return 0
    x = knapsack01(n-1,W)
    if W < weights[n]:
        return x
    else:
        y = knapsack01(n-1,W-weights[n]) + values[n]
        return max(x, y)


def knapsack01_memoisering(n,W):
    K = [[None for _ in range(n+1)] for _ in range(W)]
    print(K)
    for j in range(W):
        print(j)
        K[0][j] = 0
    for i in range(n):
        for j in range(W):
            x = K[i-1][j]
            if j < weights[n]:
                K[i][j] = x
            else:
                y = K[i-1][j-weights[n]] + v[n]
                K[i][j] = max(x,y)
    return K

n = len(values)
W = 10
print(knapsack01_memoisering(n,W))