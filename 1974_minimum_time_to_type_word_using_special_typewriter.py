

class Solution:
    def minTimeToType(self, word: str) -> int:
        alpha =[chr(x) for x in range(ord('a'), ord('z') + 1)]
        prev = "a"
        t = 0
        for i in range(len(word)):
            a = abs(alpha.index(word[i])-alpha.index(prev))
            b = 26-abs(alpha.index(prev)-alpha.index(word[i]))
            print(a,b)
            t+=min(a,b)+1
            prev = word[i]
        return t            
        