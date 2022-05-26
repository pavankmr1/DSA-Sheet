from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr,n):
    curSum = 0
    preSum = 0
    maxSum = 0 

    for i in range (n):
        if (i==0):
            curSum=arr[i]

        else:
            curSum=max(arr[i],preSum+arr[i])

        preSum = curSum
        maxSum = max(maxSum,curSum)
    return maxSum

def takeInput():
    n =int(input())

    if(n==0):
        return list(),n
    
    arr =list(map(int, stdin.readline().strip().split(" ")))

    return arr, n

arr, n = takeInput()
print(maxSubarraySum(arr,n))