def findDuplicate(arr, n):
    #https://www.youtube.com/watch?v=8ci8WfQ6cns
    
    for i in range(n):
        # Use array indices to store visited state of each element.
        index = abs(arr[i])-1

        # Mark as visited by multiplying with '-1'.
        arr[index] *=-1

        # In case of duplicate, this will become +ve.
        if arr[index]>0:
            return abs(arr[i])

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
print(findDuplicate(arr,10))
