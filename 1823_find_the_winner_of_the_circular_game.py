# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def findwinner(l,k, curr):
            if len(l)==1:
                return l[0]
            curr = (curr+k-1)%(len(l))
            l.pop(curr)
            return findwinner(l,k,curr)
        return findwinner(list(range(1,n+1)),k,0)
        
            
                