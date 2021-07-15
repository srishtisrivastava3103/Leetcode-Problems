#https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        
        maxtillnow = float('-inf')-1
        maxendhere = 0
        for i in range(0,len(a)):
            maxendhere+=a[i]
            if maxendhere>maxtillnow:
                maxtillnow = maxendhere
            if maxendhere<0:
                maxendhere = 0
        return maxtillnow
            