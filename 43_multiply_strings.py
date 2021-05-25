# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        s1 = ""
        ts = 0
        c = 0
        for i in range(len(num2)-1,-1,-1):
            s1 = ""
            carry = 0
            for j in range(len(num1)-1,-1,-1):
                p = ((ord(num1[j])-48)*(ord(num2[i])-48))+carry
                units = p%10
                carry = p//10

                s1 = str(units)+s1

            s1 = str(carry)+s1+('0'*c)
            c+=1
            ts = ts+int(s1)

        return str(ts)