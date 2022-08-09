# keeping one element i.e i as fixed and then use two sum approach

from sys import stdin, stdout, setrecursionlimit

def findTriplets(arr,n, k):

    ans = list()

    # Sorting the arrayList
    arr = sorted(arr)

    i =0
    while i<n:

        target = k - arr[i]

        low,high = i+1,n-1

        while low<high:
            sum = arr[low] +arr[high] 

            if sum < target:
                low += 1
            elif sum > target:
                high -= 1
            
            else:
                x,y = arr[high],arr[low]
                ans.append([arr[i],x,y])

                # Increment low pointer until we reach a different number
                while low<high and arr[low] ==x:
                    low += 1
                # Decrementing last pointer until we reach a different number
                while low<high and arr[high] ==y:
                    high -= 1
        
        # Ensuring that we dont encounter duplicate values for arr[i]
        while i+1 < n and arr[i] == arr[i+1]:
            i+=1
        
        i+=1
    return ans
    



