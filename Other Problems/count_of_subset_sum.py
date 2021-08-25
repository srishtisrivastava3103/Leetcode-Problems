def countSubsetSum(arr,X):
    dp = [[0]*(X+1) for i in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(len(dp[1])):
            if j==0:
                dp[i][j] = 1

            elif i==0:
                dp[i][j] = 0
            elif arr[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-arr[i-1]]
    # print(dp)
    return dp[-1][-1]
countSubsetSum([3,3,3,3],6)
                
          