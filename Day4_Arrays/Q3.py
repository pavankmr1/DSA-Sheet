class Solution:
    def longestConsecutive(self,nums):
        longest_Streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num +=1
                current_streak += 1

            longest_Streak = max (longest_Streak, current_streak)
        
        return longest_Streak

a = Solution()
print(a.longestConsecutive([100,4,200,1,3,2]))