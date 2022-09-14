def uniqueElement(arr,n):

    if n== 1:
        return arr[0]
    

    for i in range(0,n-1,2):
        # If adjacent elements are not equal then update answer
        if arr[i] != arr[i+1]:
            answer = arr[i]
            break

    # Update answer
    if arr[n-2] != arr[n-1]:
        answer = arr[n-1]
        
    return answer

    pass

