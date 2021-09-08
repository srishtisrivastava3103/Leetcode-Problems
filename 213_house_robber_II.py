# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)-1<=2:
            return max(nums)
        dp = [-1]*(len(nums)-1)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[0]+nums[2],nums[1])
        for i in range(3,len(nums)-1):
            dp[i] = max(nums[i]+dp[i-2],nums[i]+dp[i-3],dp[i-1])
        x = dp[-1]
        nums = nums[::-1]
        dp = [-1]*(len(nums)-1)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[0]+nums[2],nums[1])
        for i in range(3,len(nums)-1):
            dp[i] = max(nums[i]+dp[i-2],nums[i]+dp[i-3],dp[i-1])
        return max(dp[-1],x)
        