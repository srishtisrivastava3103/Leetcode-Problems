#https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        half = n//2 if n%2==0 else n//2+1
        return (pow(5,half,1000000007) * pow(4,n-half,1000000007))%1000000007

