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
    for city in order_list[1:]:
        if adjacency_matrix[last][city] == maxsize:
            return "umulig"
        else:
            price += adjacency_matrix[last][city]
        last = city
    return price

def Floyd_Warshall(matrix, n):
    D_0 = matrix
    for k in range(n): #For hver mellomnode
        for i in range(n): #For hver rad i matrisen
            for j in range(n): #For hver element i raden
                D_0[i][j] = min(D_0[i][j],D_0[i][k] + D_0[k][j])
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

