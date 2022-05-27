from sys import stdin
def maximunProfit(prices):
    n = len(prices)
    maxProfit =0

    for i in range(n-1):

        buy = prices[i]
        curMaxProfit=0

        for j in range(i+1,n):
            curMaxProfit=max(curMaxProfit,(prices[j]-buy))
        
        maxProfit=max(maxProfit,curMaxProfit)
    return maxProfit
prices = list(map(int,stdin.readline().strip().split()))
print(maximunProfit(prices))