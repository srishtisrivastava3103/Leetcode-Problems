# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxstsum = float('-inf')
        minstsum = float('inf')
        tempmax = 0
        tempmin = 0
        for i in range(len(nums)):
            tempmax+=nums[i]
            if tempmax>maxstsum:
                maxstsum = tempmax
            if tempmax<0:
                tempmax = 0
                
            tempmin+=nums[i]
            if tempmin<minstsum:
                minstsum = tempmin
            if tempmin>0:
                tempmin = 0
        if sum(nums)==minstsum:
            return maxstsum
        return max(maxstsum, sum(nums)-minstsum)
                
            
        