from sys import stdin
def missingAndRepeating(arr,n):
    r=0
    m=0
    for i in range(n):
        if(arr[abs(arr[i])-1] >0):
            arr[abs(arr[i])-1] *=-1
        else:
            r=abs(arr[i])
            
    for i in range(n):
        if(arr[i] > 0):
            m=i+1
    ans =m,r
    return ans

arr=list(map(int,stdin.readline().strip().split(" ")))
print(arr, len(arr))


        

