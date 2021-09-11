# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
            
        # list is sorted in descending order, return reversed.
        if i == -1:
            return nums.reverse()
        
        # find the index j where nums[j] is larger than nums[i] and swap.
        for j in reversed(range(len(nums))):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        
        # sort the rest of list in ascending order.
        j, k = i+1, len(nums)-1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j+=1
            k-=1
