#https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recurse(s,score,n):
            if score<0:
                return
            if len(s)>2*n:
                return
            if len(s)==2*n and score==0:
                ans.append(s)
                return
            recurse(s+"(",score+1,n)
            if score>0:
                recurse(s+")", score-1, n)
        recurse("",0,n)
        return ans
                
        