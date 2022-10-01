def uniqueElement(arr,n):

    low =0
    high = n-1

    # Do binary search
    while low < high:

        # calculate mid
        mid = (low + high) // 2

        # update low and high

        if (mid%2 ==1 and arr[mid]==arr[mid-1]) or (mid%2 ==0 and arr[mid]== arr[mid +1]) :
            low = mid +1

        else :
            high = mid
        
    return arr[low]
