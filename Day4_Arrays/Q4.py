from asyncio import current_task


class Solution:
    def longestSubsetWithZeroSum(self,arr):
        maxLen =0
        n = len(arr)

        for i in range(n):
            currSum =0

            for j in range(i,n):
                currSum+=arr[j]

                if currSum ==0:
                    maxLen = max(maxLen,j-i+1)
        return maxLen

a = Solution()
print(a.longestSubsetWithZeroSum([1,3,-1,4,-4,-2]))