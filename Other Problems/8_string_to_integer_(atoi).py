# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        ei = 0
        if len(str)==0:
            return 0
        for i in range(len(str)):
            if not(48<=ord(str[i])<58 or ord(str[i])==43 or ord(str[i])==45):
                if i==0:
                    return 0

                break
            if (ord(str[i])==45 or ord(str[i])==43) and i>0:
                break
                
            ei = i
        try:
            k = int(str[:ei+1])
            if k > 2**31 -1:
                return 2**31-1 
            if k < -2**31:
                return -2**31 
            return k
        except:
            return 0

        