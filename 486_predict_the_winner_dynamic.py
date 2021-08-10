# https://leetcode.com/problems/predict-the-winner

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        l = [[[-1,-1] for i in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)):
            l[i][i][0] = nums[i]
            l[i][i][1] = 0
            if i+1<len(nums):
                l[i][i+1][0] = max(nums[i],nums[i+1])
                l[i][i+1][1] = min(nums[i],nums[i+1])
        k = 2
        i = 0
        while k-i+1<=len(nums):
            i = 0
            while i+k<len(nums):
                l[i][i+k][0] = max(nums[i]+l[i+1][i+k][1],nums[i+k]+l[i][i+k-1][1])
                l[i][i+k][1] = sum(nums[i:i+k+1])-l[i][i+k][0]
                i+=1
            i=0
            k+=1

        # for j in l:       
        #     print(j)
        if l[0][len(nums)-1][0]>=(sum(nums)- l[0][len(nums)-1][0]):
            return True
        return False
