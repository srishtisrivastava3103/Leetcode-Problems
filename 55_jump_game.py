# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        obstacle = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]==0 and obstacle==-1:
                obstacle = i
            if obstacle>-1 and i+nums[i]>obstacle:
                obstacle = -1
            # print(obstacle)   
        if obstacle == -1:
            return True
        return False
        
