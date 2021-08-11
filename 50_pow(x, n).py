# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n==0:
                return 1
            if n%2==0:
                return x**(n//2)*pow(x,n//2)
            else:
                return (x**(n//2))*x*pow(x,n//2)
        if n<=-2147483648:
            if x==1 or x==-1:
                return 1
            return 0
        ans = pow(x,abs(n))
        if n<0:
            return 1/ans
        return ans

        