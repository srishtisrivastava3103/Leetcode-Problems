# https://practice.geeksforgeeks.org/problems/coin-change2448/1#

class Solution:
    def count(self, S, m, n): 
        # code here 
        dp = [[-1]*(n+1) for i in range(m+1)]
        for i in range(len(dp)):
            for j in range(len(dp[1])):
                if i==0 and j!=0:
                    dp[i][j] = 0
                elif j==0:
                    dp[i][j] = 1
                elif S[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-S[i-1]]+dp[i-1][j]
        return dp[-1][-1]

