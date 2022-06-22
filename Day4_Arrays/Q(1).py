from sqlite3 import complete_statement
from typing import List


class Solution():
    def twoSum(self,nums:List[int], target:int) -> List[int]:
        hashmap ={}
        ans =[]
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                 ans.append([nums[i],complement])
            hashmap[nums[i]] = i
        return ans
a = Solution()
print(a.twoSum([1,2,3,4,5],5))
# It turns out we can do it in one-pass. While we are iterating and inserting elements into the hash table,
#  we also look back to check if current element's complement already exists in the hash table. 
# If it exists, we have found a solution and return the indices immediately.