# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from bisect import bisect_left
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        i1 = bisect_left(nums, target)
        i2 = i1+1
        if i1>len(nums)-1 or nums[i1]!=target:
            return [-1,-1]
        while i2<len(nums):
            if nums[i2]!=target:
                break
            i2+=1
        return [i1, i2-1]    
        
        
        