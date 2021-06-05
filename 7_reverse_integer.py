# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(abs(x))
        l=list(s)
        l.reverse()
        s=''.join(l)
        y=int(s)
        if(x<0):
            y=y*(-1)
        if -2147483648<=y<=2147483647:
            return y
        else:
            return 0
        


            
        