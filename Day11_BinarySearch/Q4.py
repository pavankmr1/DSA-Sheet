from re import I


def search(arr, target):

    n= len(arr)

    for i in range(n):
        if(arr[i]==target):
            return i
    
    return -1