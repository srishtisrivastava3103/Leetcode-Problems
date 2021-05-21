# https://leetcode.com/problems/count-servers-that-communicate/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows=[0]*len(grid)
        cols=[0]*len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i]+=1
                    cols[j]+=1
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and rows[i]+cols[j] > 2:
                    res+=1
        return res
                    
                    
            
                