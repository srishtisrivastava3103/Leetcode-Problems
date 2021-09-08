# https://leetcode.com/problems/house-robber/


#Method -1
# Recursion with @lru_cache (Just recursion will give TLE)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        @lru_cache()
        def houserob(n):
            if n==0 or n==1:
                return nums[n]
            if n<1:
                return 0
            return max(nums[n]+houserob(n-2),nums[n]+houserob(n-3),houserob(n-1))
        return houserob(len(nums)-1)