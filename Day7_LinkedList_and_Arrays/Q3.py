from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10**7)

def findTriplets(arr,n,k):

    # Set to keep the track of visited triplets.
    visited = set()
    ans = list()

    for i in range (n-2):
        for j in range (i+1,n-1):
            for k in range (j+1,n):
                # If we find a valid triplet
                if arr[i]+arr[j]+arr[k] == k:
                    triplet = [arr[i], arr[j], arr[k]]
                    # Sorting the triplet track distinct triplets.
                    triplet.sort()
                    triplet = tuple(triplet)
                    if triplet not in visited:
                        visited.add(triplet)
    
    for i in visited:
        ans.append(list(i))
    
    return ans
    