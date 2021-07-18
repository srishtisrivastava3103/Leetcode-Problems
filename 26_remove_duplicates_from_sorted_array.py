# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            k=nums[i]
            j=i+1
            while j<len(nums):
            
                if k==nums[j]:
                    nums.pop(j)
                else:
                    j+=1
            i+=1
        return len(nums)