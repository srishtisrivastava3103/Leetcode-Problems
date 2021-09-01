# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1

#Here lrs = abd
def lrs(s):
    dp = [[-1]*(len(s)+1) for i in range(len(s)+1)]
    for i in range(len(dp)):
        dp[i][0] = 0
        dp[0][i] = 0
    for i in range(1,len(dp)):
        for j in range(1,len(dp)):
            if s[i-1]==s[j-1] and i!=j:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]
lrs("aabebcdd")