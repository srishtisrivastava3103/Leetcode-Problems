

def knapsack_recursive(wt,val,i, capacity):
    if wt==0 or val==0 or capacity==0 or i>=len(wt):
        return 0
    if wt[i]>capacity:
        return knapsack_recursive(wt,val,i+1,capacity)
    else:
        return max((val[i]+knapsack_recursive(wt,val,i+1,capacity-wt[i])),knapsack_recursive(wt,val,i+1,capacity))
knapsack_recursive([10,20,30],[60,100,120],0,50)
    
    