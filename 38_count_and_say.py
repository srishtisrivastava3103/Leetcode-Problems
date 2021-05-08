class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        ans = self.countAndSay(n-1)
        tans = ""
        i = 1
        k = 1
        while i<len(ans):
            if ans[i-1]==ans[i]:
                k+=1
            else:
                tans += str(k)+ans[i-1]
                k=1
            i+=1
        tans += str(k)+ans[i-1]

        return tans
