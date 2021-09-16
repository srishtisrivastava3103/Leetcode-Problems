# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue

            l = i+1
            r = len(nums)-1
            while(l<r):
                s = a+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
