# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        f=1
        if dividend == 0:
            return 0
        if dividend^divisor<0:
            f = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = math.exp(math.log(dividend)-math.log(divisor))
        ans = math.trunc(ans)
        return (min(2**31-1, f*ans))