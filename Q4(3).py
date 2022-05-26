def maxSubarraySum(arr,n):
    maxTillNow = arr[0]
    maxEnding = 0

    for i in range(n):
        maxEnding =  maxEnding+arr[i]
        # when ever we get into negative sum we will make it zero because it was no longer needed
        #BY MAKING IT Zero we can start new let's understand the given example 
        #first elment is -2 as we cannot carry -ve sum we wil not consider -2 so max sum will be zero
        #next element is -3 as it is <0 we wil not consider and make the sum =0
        #next is 4 as it is >0 we will consider for our sum so now the sum is 4
        #next element is -1 when we add it to 4 we get 3 as this is +ve we waant it
        #next is -2 whwn we add we get 1 still it is +ve so we want it 
        #next is 5 adding 5 we get 6 , next if we add -3 the max is getting lesser so -3 we will not consider
        if maxEnding<0:
            maxEnding=0
        elif(maxTillNow<maxEnding):
            maxTillNow = maxEnding

    return maxTillNow
my_array = [-2, -3, 4, -1, -2, 5, -3]  
# printing the maximum subarray sum for the users  
print("Maximum Subarray Sum:", maxSubarraySum(my_array, len(my_array)))