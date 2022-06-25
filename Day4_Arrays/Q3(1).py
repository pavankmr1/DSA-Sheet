class Solution:
    def longest_Streak(self,nums):
        if not nums: return 0

        nums.sort()

        longest_Streak =1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_Streak = max(current_streak,longest_Streak)
                    current_streak = 1

        return max(current_streak,longest_Streak)

a = Solution()
print(a.longest_Streak([100,4,200,1,3,2]))