# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(kapasitet, vekter, verdier, antall_elementer):
    K = [[0 for x in range(kapasitet + 1)] for x in range(antall_elementer + 1)]

    # Build table K[][] in bottom up manner
    for i in range(antall_elementer + 1):
        for w in range(kapasitet + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif vekter[i - 1] <= w:
                K[i][w] = max(verdier[i - 1] + K[i - 1][w - vekter[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[antall_elementer][kapasitet]

def main():
    Kapasitet = 30
    Priser = [5,4,16]
    Vekter = [6,6,20]
    antall_elementer = 3
    print(knapSack(Kapasitet, Vekter, Priser, antall_elementer))

main()