# comparator to sort items
def compare(a):
    return a[1]/a[0]

def maximumValue(item,n,w):

    # sort items according to value/weight
    items = sorted(items, key= compare, reverse=True)

    maxValue = 0
    currWeight = 0

    for i in range(n):
        if currWeight + items[i][0] <= w:
            currWeight += items[i][0]
            maxValue += items[i][1]
        else:
            remainingWeight = w-currWeight
        
        # Pick a fraction of current item
        maxValue += items[i][1]*(remainingWeight/items[i][0])
        break

    return round(maxValue,2)