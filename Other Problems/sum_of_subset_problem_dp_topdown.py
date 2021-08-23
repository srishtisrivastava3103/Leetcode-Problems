#https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/?category[]=Dynamic%20Programming&category[]=Dynamic%20Programming&page=4&query=category[]Dynamic%20Programmingpage4category[]Dynamic%20Programming#

class Solution:
    def isSubsetSum (self, N, arr, sum):
        nums = arr
        # code here 
        dp = [[False]*(sum+1) for i in range(len(nums)+1)]
        for item in range(len(dp)):
            for currsum in range(len(dp[0])):
                if item==0:
                    dp[item][currsum] = False
                if currsum==0:
                    dp[item][currsum]=True
                elif nums[item-1]>currsum:
                    dp[item][currsum] =dp[item-1][currsum]
                else:
                    dp[item][currsum] = dp[item-1][currsum-nums[item-1]] or dp[item-1][currsum]
                    
        # print(dp)
        return dp[-1][-1]
        
