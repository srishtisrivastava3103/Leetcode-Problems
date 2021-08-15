# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums):
        res = []
        def powerset(nums,i,curr):
            if i==len(nums):
                res.append(curr)
                return
            powerset(nums,i+1,curr+[nums[i]])
            powerset(nums,i+1,curr)
        powerset(nums,0,[])
        return res
            
