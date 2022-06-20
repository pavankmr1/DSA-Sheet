def reversePairs(arr,n):
    ans =0

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > 2 *arr[j]:
                ans += 1

    return ans

arr = [1,2,3,2,3,1]
print (reversePairs(arr,len(arr)))