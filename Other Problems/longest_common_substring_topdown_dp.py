def lcs(a,b):
    dp = [[-1]*(len(b)+1) for i in range(len(a)+1)]
    for i in range(len(dp)):
        dp[i][0] = 0
    for i in range(len(dp[0])):
        dp[0][i] = 0
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if a[i-1]==b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp[-1][-1])
lcs("abedfhr","abcdgh")