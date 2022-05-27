from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr,n):
    ans =0
    #where the outer loop points to the left boundary
    for i in range(n):
        #the inner loop points to the outer boundary of the subarray. 
        for j in range(i,n):
            tempSum =0
            #Using another loop inside, find the sum of this subarray
            for k in range(i,j+1):
                tempSum += arr[k]
            #Compare it with the maximum subarray sum obtained so far
            ans = max(ans,tempSum)
    #return the maximum sum found.
    return ans

#taking input using fast I/O
def takeInput() :
    n = int(input())

    if(n==0):
        return list(),n

    # If the input contains a space separated line of int, like-
    # 1 3
    # I can map store it in an array using the map() function
    # arr = map(int,sys.stdin.readline().split())
    # or even in two separate variables, by
    # n,m = map(int,sys.stdin.readline().split())

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr,n

#main
arr,n = takeInput()
print(maxSubarraySum(arr, n))