from sys import stdin

maxsize = 9223372036854775807

# stdin = open("input.txt")

def shortest_path(order_list, adjacency_matrix, cities):
    #Husk at hun skal returnere til byen hun kom fra!
    order_list.append(order_list[0])

    #Lag kortest vei alle til alle matrise:
    adjacency_matrix = Floyd_Warshall(adjacency_matrix,cities)

    price = 0
    last = order_list[0] #er lik startnoden først
    for x in range(1,len(order_list)):
        next = order_list[x]
        if adjacency_matrix[last][next] == maxsize:
            return "umulig"
        else:
            price += adjacency_matrix[last][next]
        last = next
    return int(price)

def Floyd_Warshall(matrix, k):
    n = k
    D_0 = matrix
    for k in range(n):
        d_k = [[0]*n for x in range(n)]
        for i in range(n): #For hver rad i matrisen
            for j in range(n): #For hver element i raden
                d_k[i][j] = min(D_0[i][j],D_0[i][k] + D_0[k][j])
        D_0 = d_k
    return D_0



def convert(str):
    if int(str) == -1:
        return maxsize
    return int(str)

testcases = int(stdin.readline())
for test in range(testcases):
    cities = int(stdin.readline())
    order_list = [int(city) for city in stdin.readline().split()]
    adjacency_matrix = [[convert(weight) for weight in stdin.readline().split()] for city in range(cities)]
    print(shortest_path(order_list, adjacency_matrix, cities))

