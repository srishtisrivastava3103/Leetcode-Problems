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


#Method - 2
# Memoization

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        dp = [-1]*len(nums)
        def houserob(n):
            if n==0 or n==1:
                return nums[n]
            if n<1:
                return 0
            if dp[n]!=-1:
                return dp[n]
            dp[n] = max(nums[n]+houserob(n-2),nums[n]+houserob(n-3),houserob(n-1))
            return dp[n]
        return houserob(len(nums)-1)

# Method - 3
# Iterative DP

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        dp = [-1]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[0]+nums[2],nums[1])
        for i in range(3,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],nums[i]+dp[i-3],dp[i-1])
        return dp[-1]