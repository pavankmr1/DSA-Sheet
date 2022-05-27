from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def sort012(arr,n):

    #STORING COUNT OF 0 1 2
    count=[0 0 0]

    for i in range (n):
        count[arr[i]] +=1

    i=0

    for j in range(3):
        while(count[j]):
            arr[i]= 0+j
            i+=1
            count[j]-=1

def takeInput():
    n = int(input())
    if n==0:
        return list(),0

    arr=list(map(int, stdin.readline().strip().split(" ")))

    return arr,n

def printAnswer(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()

#main
t = int(input().strip())
for i in range(t):
    arr,n = takeInput()
    sort012(arr,n)
    printAnswer(arr,n)
