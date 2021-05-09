# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ch = [word[0]]
        fr = [1]
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                fr[-1]+=1
            else:
                ch.append(word[i])
                fr.append(1)
        m = 0
        for i in range(4,len(ch)):
            if ch[i-4:i+1]==['a','e','i','o','u']:
                m = max(m,sum(fr[i-4:i+1]))
        return m

