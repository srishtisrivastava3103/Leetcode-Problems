# https://leetcode.com/problems/map-of-highest-peak/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        r, c = len(isWater), len(isWater[0])
        ans = [[-1]*c for j in range(r)]
        q = []
        for i in range(r):
            for j in range(c):
                if isWater[i][j] == 1:
                    isWater[i][j] = -1
                    q.append((i,j,0))
        print(q)
        while q:
            (i,j,h) = q.pop(0)
            ans[i][j] = h
            for a,b in [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]:
                if a>=0 and a<r and b>=0 and b<c and isWater[a][b]>=0:
                    isWater[a][b] = -1
                    q.append((a,b,h+1))
        return ans