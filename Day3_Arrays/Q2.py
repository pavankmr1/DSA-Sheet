def findMajorityElement(arr,n):

    for i in range(n):

        maxCount =0

        for j in range(n):

            if arr[i]==arr[j]:
                maxCount +=1

        if maxCount > n/2:
            return arr[i]

    return -1
    