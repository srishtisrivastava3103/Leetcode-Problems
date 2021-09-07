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
