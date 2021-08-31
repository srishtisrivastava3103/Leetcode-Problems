# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        dp = [[-1]*(len(s)+1) for i in range(len(s)+1)]
        for i in range(len(s)):
            dp[0][i] = 0
            dp[i][0] = 0
        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]