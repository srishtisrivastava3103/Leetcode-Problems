# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        left =[]
        right = []
        s = expression
        for i in range(len(s)):
            if s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=='/':
                a = s[:i]
                b = s[i+1:]
                left = self.diffWaysToCompute(a)
                right = self.diffWaysToCompute(b)
                for l in left:
                    for r in right:
                        if s[i]=="+":
                            ans.append(int(l)+int(r))
                        elif s[i]=="-":
                            ans.append(int(l)-int(r))
                        elif s[i]=="*":
                            ans.append(int(l)*int(r))
                        else:
                            ans.append(int(l)/int(r))
        if len(ans)==0:
            ans.append(s)
        return ans

        