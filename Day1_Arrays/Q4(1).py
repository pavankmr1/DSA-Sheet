import readline
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSunarraySum(arr,n):
    ans =0
    for i in range(n):
        tempSum =0
        for j in range (i,n):
            tempSum +=arr[j]
            ans = max(ans,tempSum)
    return ans

def takeInput():
    n =int(input())

    if(n==0):
        return list(),n

    arr=list(map(int,stdin,readline().strip().split(" ")))

    return arr,n

arr, n = takeInput()
print(maxSunarraySum(arr,n))
