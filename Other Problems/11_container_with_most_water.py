# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water=0
        LP=0        # left pointer
        RP=len(height)-1    # right pointer
        while LP<RP:
            max_water=max(max_water, min(height[LP],height[RP])*(RP-LP)) # amount of water = min of the two heights * the diff of their indices
            if height[LP]<height[RP]:   # if LP's height is smaller than RP's move LP forward, otherwise more RP backward
                LP+=1
            else:
                RP-=1
        return max_water