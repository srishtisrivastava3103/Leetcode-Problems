# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1

def lcsubstring(a,b):
    dp = [[-1]*(len(b)+1) for i in range(len(a)+1)]
    for i in range(len(dp)):
        dp[i][0] = 0
    for i in range(len(dp[0])):
        dp[0][i] = 0
    max_ = 0
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                max_ = max(max_,dp[i][j])
            else:
                dp[i][j] = 0
    return max_

lcsubstring("abcde","abfce")    