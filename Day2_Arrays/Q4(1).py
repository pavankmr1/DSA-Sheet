def findDuplicate(arr,n):

    uset=set()

    for i in range(n):
        if arr[i] in uset:
            return arr[i]
        else:
            uset.add(arr[i])

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
print(findDuplicate(arr,10))