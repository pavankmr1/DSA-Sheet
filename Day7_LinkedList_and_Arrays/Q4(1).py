def getTeappedwater(arr,n):

    # Base case
    if (n==0):
        return 0
    
    totalWaterStored = 0

    # Storing leftMax and rightMax
    leftMax = [0 for i in range(n)]
    rightMax = [0 for i in range(n)]

    leftMax[0] = arr[0]
    rightMax[n-1] = arr[n-1]

    # Filling leftMax
    for i in range(1,n):
        leftMax[i] = max(leftMax[i-1],arr[i])
    

    # Filling rightMax
    for i in range (n-2,-1,-1):
        rightMax[i] = max(arr[i], rightMax[i+1])
    
    # Calcualte result
    for i in range(1,n-1):
        totalWaterStored += min(rightMax[i],leftMax[i]) - arr[i]
    
    return totalWaterStored
    


