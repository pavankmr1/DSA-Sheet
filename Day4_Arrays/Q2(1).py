class Solution:
    def fourSum(self,nums,target):
        n = len(nums)
        nums.sort()
        result = []
        #[1,1,1,2,2,-1,5,-2,-2,3,-3] for eample if we take this array
        # ^ ^ ^                   ^
        # | | |                   |
        # i j left              right
        # i points to first element , j points to next element after i 
        #left points to nxt element of j at starting and right points to last element of the array

        for i in range(n-3):
            # here doing "and" with i because if starting two elements are same then it will skip but this should not happen 
            # for the first element so we are doing and with i  
            if i and nums[i] == nums[i-1]:
                #if nums[i] == nums[i-1] this implies these are dupicates so we need to skip for duplicates
                continue
            for j in range(i+1,n-2):
                # Here also same as above
                if j!=i+1 and nums[j] == nums[j-1]:
                    continue
                total = target - nums[i]-nums[j]
                #we are asisigning total a target-nums[j]-nums[i] so that we can check with the sum of the arr[left]+arr[right]
                left,right = j+1,n-1
                #pointing left to J+1 adn right to last element
                while left < right:
                    if nums[left] + nums[right] == total:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        # if we found the desired total then we will shift both right and left pointers 
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right +1]:
                            right -=1
                    elif nums[left] + nums[right] > total:
                        # as the array is sorted and the sum is greater than total that means we ave to decrease the number 
                        # for that we have to move the right pointer by this we can decrease the sum 
                        right -= 1
                    else :
                        #as the array is sorted and the sum is lesser than total that means we have to increase  the number 
                        #for that we have to move the left pointer by this we can increse the sum
                        left += 1
        return result