# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

dp = [[-1]*4 for i in range(4)]
def palinpartition(s,i,j):
    print("count")
    if i>=j:
        dp[i][j] = 0
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i:j+1]==s[i:j+1][::-1]:
        dp[i][j] = 0
        return 0
    ans = float('inf')
    for k in range(i,j):
        if dp[i][k]!=-1:
            left=  dp[i][k]
        else:
            left = palinpartition(s,i,k)
        if dp[k+1][j]!=-1:
            left=  dp[k+1][j]
        else:
            right = palinpartition(s,k+1,j)
        
        temp = left+right+1
        ans = min(ans,temp)
    dp[i][j] = ans
    return ans
palinpartition("aaaa",0,3)