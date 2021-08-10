# https://leetcode.com/problems/predict-the-winner/
# Recursive Approach
# Same code works in java but gives TLE in Python in the second last test case.
# Java equivalent of this code is given below.

class Solution:
    def PredictTheWinner(self, nums):
        def predict(s, nums, st, end, chance, half):
            if end<st:
                return 0
            if chance==True:
                return max(nums[st]+predict(s,nums,st+1,end,not chance, half),   
                        nums[end]+predict(s,nums,st,end-1,not chance, half))
            else:
                return min(predict(s,nums,st+1,end,not chance, half),   
                        predict(s,nums,st,end-1,not chance, half))
        half = sum(nums)//2
        s = predict(0,nums,0,len(nums)-1,True,half)
        if s>=half:
            return True
        return False



 # Java
            
'''class Solution {
    public int predict(int[] nums, int st, int end, int chance)
    {
        if(st>end)
            return 0;
        if (chance==1)
            return Math.max(nums[st]+predict(nums,st+1,end,0),nums[end]+predict(nums,st,end-1,0));
        else
            return Math.min(predict(nums,st+1,end,1),predict(nums,st,end-1,1));

    }
    public boolean PredictTheWinner(int[] nums) {
        int s = predict(nums, 0, nums.length-1, 1);
        int sum = 0;
        for(int i=0;i<nums.length;i++)
            sum+=nums[i];
        if(s>=(sum-s))
            return true;
        return false;
            
        
    }
}'''