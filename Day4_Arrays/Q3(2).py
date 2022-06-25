class Solution:
    def longest_Streak(self,nums):
        longest_streak =0
        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak= 1

                while current_num+1 in num_set:
                    current_num = current_num+1
                    current_streak += 1

                longest_streak = max(current_streak,longest_streak)

        return longest_streak

a = Solution()
print(a.longest_Streak([100,4,200,1,3,2]))

# Time complexity : O(n).

# Although the time complexity appears to be quadratic due to the while loop nested within the for loop,
#  closer inspection reveals it to be linear. Because the while loop is reached only when currentNum marks the beginning of a sequence 
# (i.e. currentNum-1 is not present in nums), the while loop can only run for nn iterations throughout the entire runtime of the algorithm. 
# This means that despite looking like O(n \cdot n)O(n⋅n) complexity, the nested loops actually run in O(n + n) = O(n)O(n+n)=O(n) time.
#  All other computations occur in constant time, so the overall runtime is linear.
