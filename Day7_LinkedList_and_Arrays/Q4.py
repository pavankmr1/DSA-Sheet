def getTrappedWater(arr,n):

    # Result
    ans =0

    # Traversing
    for i in range(1,n-1):

        maxLeftHeight = arr[i]
        for j in range(i,-1,-1):

            maxLeftHeight = max(arr[j],maxLeftHeight)
        
        maxRightHeight = arr[i]
        for j in range(i,n):

            maxRightHeight = max(arr[j],maxRightHeight)
        
        # Calculation
        ans += min(maxLeftHeight,maxRightHeight)-arr[i]
    
    return ans
    