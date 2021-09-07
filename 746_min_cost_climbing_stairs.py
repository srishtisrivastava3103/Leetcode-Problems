# https://leetcode.com/problems/min-cost-climbing-stairs/

# We go from Recursion->Memoization->Top Down


# Recursion will give TLE
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost+=[0]
        def costing(i):
            if i==0 or i==1:
                return cost[i]
            return min(cost[i]+costing(i-1),cost[i]+costing(i-2))
        return costing(len(cost)-1)

# We can use memoization in two ways

# @lru_cache() decorator

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost+=[0]
        @lru_cache()
        def costing(i):
            if i==0 or i==1:
                return cost[i]
            return min(cost[i]+costing(i-1),cost[i]+costing(i-2))
        return costing(len(cost)-1)

# Using memoization explicitly

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost+=[0]
        dp = [-1]*(len(cost)+1)
        def costing(i):
            if i==0 or i==1:
                return cost[i]
            if dp[i]!=-1:
                return dp[i]
            
            dp[i] = min(cost[i]+costing(i-1),cost[i]+costing(i-2))
            return dp[i]
        return costing(len(cost)-1)


# Top Down Approach (DP Iterative)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost+=[0]
        dp = [-1]*len(cost)
        for i in range(len(cost)):
            if i==0 or i==1:
                dp[i] = cost[i]
            else:
                dp[i] = min(cost[i]+dp[i-1],cost[i]+dp[i-2])
        return dp[-1]
