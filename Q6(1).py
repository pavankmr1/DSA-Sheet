from sys import stdin
def maximumProfit(prices):
    n = len(prices)
    maxProfit =0
    buy = prices[0]

    for i in range(1,n):
        if prices[i]<buy:
            buy = prices[i]

        elif prices[i]-buy>maxProfit:
            maxProfit=prices[i]-buy

    return maxProfit

prices = list(map(int,stdin.strip().split(" ")))
print(maximumProfit(prices))
