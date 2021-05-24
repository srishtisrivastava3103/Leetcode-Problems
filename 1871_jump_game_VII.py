# https://leetcode.com/problems/jump-game-vii/

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = collections.deque([0])
        mx = 0
        while queue:
            i = queue.popleft()
            for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    if j == len(s) - 1: return True
                    queue.append(j)
            mx = i + maxJump 
        return False