from collections import OrderedDict

class Solution():
    def longestSubsetWithZeroSum(self,arr):

        #Map to store the previous Sum

        presum =  OrderedDict() 
        
        sum =0 #initialize the sum of elements
        maxLen =0
        n = len(arr)

        for i in range(n):
            sum += arr[i]

            if(arr[i]==0 and maxLen ==0):
                maxLen =1
            if sum ==0:
                maxLen = i+1

            # look up for the sum in the Hash table

            if(sum in presum):
                maxLen = max(maxLen, i-presum.get(sum))
            else:
                presum[sum] = i
        return maxLen
a = Solution()
print(a.longestSubsetWithZeroSum([1,3,-1,4,-4,-2]))


        