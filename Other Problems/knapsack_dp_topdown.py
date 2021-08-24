dp = [[-1]*51 for x in range(4)]
def knapsack_topdown(w,val,i, capacity):
    for i in range(len(dp)):
        for wt in range(len(dp[0])):
            if i==0 or wt==0:
                dp[i][wt] = 0
            elif w[i-1]>wt:
                dp[i][wt] = dp[i-1][wt]
            else:
                dp[i][wt] = max(val[i-1]+dp[i-1][wt-w[i-1]],dp[i-1][wt])
    currwt = capacity  
    objects = []
    
    ## Printing the objects included in the knapsack by reversing the methos used to fill in the matrix.
    for i in range(len(dp)-1,0,-1):
        if dp[i][currwt]>dp[i-1][currwt]:
            objects.append(i)
            currwt -= w[i-1]
        i-=1
    print(objects)       
    return dp[-1][-1]
knapsack_topdown([10,20,30],[60,100,120],0,50)
    
##For this particular change there's a small decrease in the number of function call between memoization and recursive approach.
# This will work better with bigger inputs.