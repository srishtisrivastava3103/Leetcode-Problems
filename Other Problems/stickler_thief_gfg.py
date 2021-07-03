#https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        if len(a)<=2:
            return max(a)
        dp = [a[0], max(a[0],a[1])]
        for i in range(2,n):
            dp.append(max(dp[-1], dp[-2]+a[i]))
        return dp[-1]
            
