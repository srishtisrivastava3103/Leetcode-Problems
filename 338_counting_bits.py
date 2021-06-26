#https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0,1]
        if n==0:
            return [0]
        if n==1:
            return dp
            
        c = 1
        while c<n:
            k = len(dp)
            for i in range(k):
                dp.append(1+dp[i])
                c+=1
                if c==n:
                    break
        return dp
            
        

