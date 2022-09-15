def search(arr, target):

    st =0
    end = len(arr)-1

    while st <= end:

        # Get the middle element
        mid = st+(end-st) //2

        # The middle element is the one we are searching

        if arr[mid] == target:
            return mid
        
        elif arr[mid] >= arr[st]:

            # Element lies towards left of mid
            if (arr[st] <=  target and target <= arr[mid]):
                end = mid-1
            
            else:
                st = mid+1
            
        else:

            # Element lies towards right of mid
            if (arr[end] >= target and target >= arr[mid]):
                st = mid+1
            
            # element lies towards left of mid
            else:
                end = mid -1
        
        # Element not found
        return -1
        



