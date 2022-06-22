from typing import List


class Solution:
    def twoSum(self,nums:List[int], target:int) -> List[int]:
        ans =[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    ans.append([nums[i],nums[j]])

        return ans

a = Solution()
print(a.twoSum([1,2,3,4,5],5))
