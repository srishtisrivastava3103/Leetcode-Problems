dp = [[-1]*51 for x in range(3)]
def knapsack_memo(wt,val,i, capacity):
    if wt==0 or val==0 or capacity==0 or i>=len(wt):
        return 0
    if dp[i][capacity]!=-1:
        return dp[i][capacity]
    if wt[i]>capacity:
        dp[i][capacity] = knapsack_memo(wt,val,i+1,capacity)
        return dp[i][capacity]
    else:
        dp[i][capacity] = max((val[i]+knapsack_memo(wt,val,i+1,capacity-wt[i])),knapsack_memo(wt,val,i+1,capacity))
        return dp[i][capacity]
knapsack_memo([10,20,30],[60,100,120],0,50)
    
##For this particular change there's a small decrease in the number of function call between memoization and recursive approach.
# This will work better with bigger inputs.