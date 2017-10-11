from sys import stdin

Inf = 1000000000
def min_coins_greedy(coins, value):
    number_of_coins = 0
    index = 0
    while value != 0:
        current_coin = coins[index]
        if value >= current_coin:
            multiplum = int(value/current_coin)
            value -= multiplum*current_coin
            number_of_coins += multiplum
        index+=1
    return number_of_coins


def min_coins_dynamic(coins, value):
        results = [Inf] * (value + 1)
        usefulCoins = []
        for c in coins:
            if c <= value:
                results[c] = 1
                usefulCoins.append(c)
        for curVal in range(1, value + 1):
            if results[curVal] != Inf:
                continue
            best = Inf
            for c in usefulCoins:
                if c <= curVal:
                    current = 1 + results[curVal - c]
                    if current < best:
                        best = current
            results[curVal] = best
        return results[value]

def min_coins_dynamic_2(coins, value, known_results=[0]*10000):
    minCoins = value
    if value in coins:
        known_results[value] = 1
        return 1
    elif known_results[value] > 0:
        return known_results[value]
    else:
        possible_coins = [c for c in coins if c <= value]
        for coin in possible_coins:
            numCoins = 1 + min_coins_dynamic(coins,value-coin,known_results)
            if numCoins < minCoins:
                minCoins = numCoins
                known_results[value] = minCoins
    return minCoins

def count(coins, n):
    m = len(coins)
    coins.reverse()
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n + 1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(coins[i], n + 1):
            table[j] += table[j - coins[i]]

    return table[n]

def can_use_greedy(coins):
    for i in range(len(coins) - 1):
        if coins[i] % coins[i + 1] != 0:
            return False
    return True

def main():
    coins = []
    for c in stdin.readline().split():
        coins.append(int(c))
    coins.sort()
    coins.reverse()
    method = stdin.readline().strip()
    if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
        for line in stdin:
            print(min_coins_greedy(coins, int(line)))
    else:
        for line in stdin:
            print(count(coins, int(line)))

if __name__ == '__main__':
    main()