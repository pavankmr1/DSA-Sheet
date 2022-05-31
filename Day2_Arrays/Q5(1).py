from sys import stdin 
def missingAndRepeating(arr,n):
    arr.sort()
    r=0
    m=0
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            r=arr[i]

    curSum=0
    for i in range(n):
        curSum+=arr[i]
    
    actualSum=n*(n+1)//2

    m=actualSum-(curSum-r)
    ans =m,r

    return ans

arr = list(map(int,stdin.readline())).strip().split(" ")
print(arr,len(arr))
