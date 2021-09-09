# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*len(nums)
        dp[0] = 0
        for i in range(len(nums)-1):
            for j in range(1,nums[i]+1):
                if i+j<len(nums):
                    dp[i+j] = min(dp[i+j],1+dp[i])
        # print(dp)
        return dp[-1]
                
                    
                
        