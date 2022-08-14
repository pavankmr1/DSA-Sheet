denominations = [1,2,5,10,20,50,100,500,1000]

def findMinimumCoins(amount):
    coinsCount =0
    n = len(denominations)

    # Pick coins in decreasing order of their values
    for i in range(n-1,-1,-1):
        while amount >= denominations[i]:
            amount -= denominations[i]
            coinsCount += 1
    
    return coinsCount
