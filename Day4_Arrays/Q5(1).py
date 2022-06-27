# https://www.geeksforgeeks.org/count-number-subarrays-given-xor/
#refer youtube

def subarrayXor(arr,x):
    n = len(arr)

    #to store the prefix XOR

    prefXor = {}

    ans =0

    #To keep track of curr XOR

    currXor =0

    #initially XOR is 0
    prefXor[0]=1

    for i in range(n):

        #update the Xor of the current prefix

        currXor = currXor^arr[i]

        #Required value of the prefix Xor to make the Xor of the subarray equal to X

        req = x^currXor

        if(req in prefXor):
            ans+= prefXor[req]

        if currXor in prefXor:
            prefXor[currXor] = prefXor[currXor]+1
        else:
            prefXor[currXor] =1
    return ans

