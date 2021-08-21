#https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        c = 2
        while c>=0:
            for i in range(1,len(nums)-1):
                if (nums[i-1]+nums[i+1])/2==nums[i]:
                    nums[i],nums[i+1] = nums[i+1], nums[i]
            c-=1
        return nums
