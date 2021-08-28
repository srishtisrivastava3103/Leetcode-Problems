
dp = [[-1]*len("abcdgh") for i in range(len("abedfhr"))]
def lcs(i,j,a,b):
    if i==len(a) or j==len(b):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if a[i]==b[j]:
        dp[i][j] = 1+lcs(i+1,j+1,a,b)
        return dp[i][j]
    else:
        dp[i][j] = max(lcs(i+1,j,a,b),lcs(i,j+1,a,b))
        return dp[i][j]
lcs(0,0,"abedfhr","abcdgh")