# https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        q="MDCLXVI"
        v=1000
        d=2
        s=''
        for i in q:
            s=s+i*(num//v)
            num=num%v

            v=v//d
            d=2+3*(d==2)
        for i in range(1,len(q),2):
            n,c,p=q[i-1:i+2]
            s=s.replace(c+p*4,p+n)
            s=s.replace(p*4,p+c)
        return s
            
            
            
        