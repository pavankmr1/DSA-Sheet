from sys import stdin
def missingAndRepeating(arr,n):
    r =0
    m=0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]==arr[j]):
                r=arr[i]
                break
    curSum =0
    for i in range(n):
        curSum += arr[i]

    actualSum = n*(n+1)//2

    m=actualSum-(curSum-r)
    ans = m,r
    return ans

arr=list(map(int, stdin.readline().strip().split(" ")))
print(missingAndRepeating(arr,len(arr)))
