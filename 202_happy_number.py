

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=[]
        s=n
        while(s>=0):
            t=s
            s=0
            #print(t)
            while(t>0):
                r=int(t%10)
                s=s+int(r*r)
                t=int(t/10)
            if s in l:
                return False
            l=l+[s]
            if(s==1):
                return True
        return False