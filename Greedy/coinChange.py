def coinChange(totalValue, coins):
    N = totalValue
    coins.sort()
    index = len(coins) - 1
    while True:
        coinsValue = coins[index]
        if N >= coinsValue:
            print(coinsValue)
            N = N - coinsValue
        if N < coinsValue:
            index -= 1
        if N == 0:
            break


coins = [1, 2, 5, 20, 50, 100]
coinChange(201, coins)
