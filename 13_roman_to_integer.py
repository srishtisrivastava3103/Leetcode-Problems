# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        val=0
        
        for i in range(1,len(s)):
            if l.get(s[i-1])>=l.get(s[i]):
                ans=ans+l.get(s[i-1])
            else:
                ans=ans-l.get(s[i-1])
        ans=ans+l.get(s[len(s)-1])
        return ans
            
            
        