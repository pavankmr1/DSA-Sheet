def median(a,b):

    if len(a) > len(b):
        a,b = b,a
    
    n= len(a)
    m = len(b)
    low =0
    high =0

    # Binary Search
    while low <= high:
        mid = (low+high)//2
        part = (n+m+1)//2 - mid

        # If part is greater than m
        if part >m:
            low = mid+1
            continue

        leftMax = 0
        rightMin = 10**9 +1

        if mid >0:
            leftMax = max(leftMax,a[mid-1])
        if mid<n:
            leftMax = min(leftMax,b[part-1])
        if mid<n:
            rightMin = min(rightMin,a[mid])
        if part<m:
            rightMin = min(rightMin,b[part])

        
        # If leftMax is less than or greater than rightMin
        if leftMax <= rightMin:

            if (n+m) &1:
                return leftMax*1.0
            
            return (leftMax + rightMin)/2.0
        
        # If a[mid] is less than leftMax
        if a(mid) < leftMax:
            low = mid+1
        else:
            high = mid -1
    
    return -1
    
