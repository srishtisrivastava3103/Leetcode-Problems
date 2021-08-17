# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        d = {'2':"abc","3":"def","4":"ghi","5":"jkl",'6':"mno",'7':"pqrs",'8':'tuv','9':'wxyz'}
        def combination(digits,s,i):
            if i==len(digits):
                return s 
            ans = []
            for j in range(len(s)):
                for k in d[digits[i]]:
                    ans.append(s[j]+k)

            return combination(digits,ans,i+1)
        return combination(digits,list(d[digits[0]]),1)
