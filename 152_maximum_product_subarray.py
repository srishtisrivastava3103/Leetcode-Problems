# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float("inf")
    
        def path_max(nums, res):
            product = 1
            for i in range(0,len(nums)):
                product*=nums[i]
                res = max(res, product)
                if nums[i] == 0:
                    product = 1

            return res
        return max(path_max(nums, res), path_max(nums[::-1], res))
        

        