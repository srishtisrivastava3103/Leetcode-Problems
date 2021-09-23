def levenshteinDistance(str1, str2):
    # Write your code here.
    dp = [[0]*(len(str2)+1) for i in range(len(str1)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i==0 and j==0:
                dp[i][j] = 0
            elif i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif str1[i-1]==str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(1+dp[i-1][j-1],1+dp[i-1][j],1+dp[i][j-1])
    return dp[-1][-1]


from functools import lru_cache
def levenshteinDistance(str1, str2):
    # Write your code here.
    @lru_cache()
    def solve(i,j):
        if i<0 and j<0:
            return 0
        elif i<0 and j>=0:
            return j+1
        elif j<0 and i>=0:
            return i+1
        elif str1[i]==str2[j]:
            return solve(i-1,j-1)
        else:
            return min(1+solve(i-1,j-1),1+solve(i-1,j),1+solve(i,j-1))
    return solve(len(str1)-1,len(str2)-1)		


