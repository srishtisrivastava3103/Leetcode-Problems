# https://leetcode.com/problems/decode-string/


#Method-1 Using stack
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        i = 0
        ans = ""
        c = 0
        while i<len(s) :
            if s[i]!=']':
                if s[i].isnumeric():
                    num = ""
                    while i<len(s) and s[i].isnumeric():
                        num+=s[i]
                        i+=1
                    st.append(int(num))
                else:
                    st.append(s[i])

                    i+=1
            else:
                c-=1
                k = len(st)-st[::-1].index('[')-1
                temp = ''.join(st[k+1:])*int(st[k-1])
                st = st[:k-1]
                st.append(temp)
                i+=1
        return ''.join(st)
