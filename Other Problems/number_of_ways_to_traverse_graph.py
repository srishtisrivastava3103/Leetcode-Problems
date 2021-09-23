# Traverse a to the bottom right end of the graph if you can move only right and down. 

# Recursive Solution

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    def solve(w,h):
        if w==width-1 or h==height-1:
            return 1
        else:
            return solve(w+1,h)+solve(w,h+1)
    return solve(0,0)


# Top Down DP

def numberOfWaysToTraverseGraph(width, height):
	dp = [[0]*width for i in range(height)]
	for i in range(len(dp)):
		for j in range(len(dp[0])):
			if i==0 and j==0:
				dp[i][j] = 0				
			elif i==0 or j==0:
				dp[i][j] = 1
			else:
				dp[i][j] = dp[i-1][j]+dp[i][j-1]
	return dp[-1][-1]
