#https://leetcode.com/problems/count-good-numbers/

#This method uses binary exponentiation to implement power function.
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(val,powe):
            if powe==0:
                return 1
            p= power(val,powe//2)
            return (p*p%1000000007*(1 if powe%2==0 else val))%1000000007
        return (power(4, n//2)*power(5, n//2)*(1 if n%2==0 else 5))%1000000007
    