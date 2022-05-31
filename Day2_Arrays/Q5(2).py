from sys import stdin
def missingAndRepeating(arr,n):
    countNumbers = [0]*n

    for i in range(n):
        countNumbers[arr[i]-1] += 1

    m =0
    r=0

    for i in range(n):
        if(countNumbers[i] == 0):
            m =i+1
        if(countNumbers[i] ==2):
            r=i+1

    ans =m, r
    return ans

arr= list(map(int, stdin.readline().strip().split(" ")))
print(arr, len(arr))