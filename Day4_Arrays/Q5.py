from operator import xor


def subarrayXor(arr,n,m):
    ans =0

    for i in range (n):


        xorSum = 0 # Store XOR of current subarray

        for j in range (i,n):

            xorSum = xorSum ^ arr[j]   

            #if xorSum is equal to given value then increase by 1

            if  (xorSum==m):
                ans += 1

        return ans

def main():
    arr = [4,2,2,6,4]
    n = len(arr)
    m =6

    print("Number of subarrays having given XOR is",subarrayXor(arr,n,m))

if __name__ == "__main__":
    main()