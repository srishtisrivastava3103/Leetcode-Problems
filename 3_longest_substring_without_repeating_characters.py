# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxcount=0
        seen=deque()
        for i in s:
            if i in seen:
                while(seen.popleft()!=i):
                    pass
            seen.append(i)
            if len(seen)>maxcount:
                maxcount=len(seen)
        return maxcount
            
        
        
        