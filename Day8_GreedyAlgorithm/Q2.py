from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPlatforms(at,dt,n):

    # sort both the arrays
    at.sort()
    dt.sort()

    # Indicates the number of platforms needed at a time
    curNumberOfPlatforms =0

    # Variable to store the minimum nuber of platforms
    minNumberPlatforms =0

    i,j = 0,0
    while(i<n and j<n):

        # if the next event in sorted order is arrival, increment count of platforms needed
        if at[i] <= dt[j]:
            curNumberOfPlatforms += 1
            i += 1
        
        # Else decrement count of platforms needed
        else:
            curNumberOfPlatforms -= 1
            j += 1
        
        # Update minimum number of platforms.
        minNumberPlatforms = max(minNumberPlatforms,curNumberOfPlatforms)
    
    # return the minimum number of platforms needed
    return minNumberPlatforms


# Taking The input
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int,stdin.readline().strip().split(" ")))
    dt = list(map(int,stdin.readline().strip().split(" ")))

    return at,dt,n

# Main 
Tst = input() # Number of test cases
T = int(Tst)

while T >0:
    T -=1
    at,dt,n = takeInput()
    minNumberPlatforms = calculateMinPlatforms(at,dt,n)
    print(minNumberPlatforms)
