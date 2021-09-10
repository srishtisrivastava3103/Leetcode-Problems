https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        elem = nums[0]
        sums = [elem] * len(nums)
        for i in range(1,len(nums)):
            if sums[i-1]<0:
                sums[i] = nums[i]
                continue
            else:
                sums[i] = sums[i-1] + nums[i]
            print(sums)
        return max(sums)