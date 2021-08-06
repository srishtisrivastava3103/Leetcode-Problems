# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s,i):
            if i<len(s)//2:
                s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]
                return reverse(s,i+1)
            return s
        return reverse(s,0)
                
# if __name__=="__main__":
#     print(Solution().reverseString(["h","e","l","l","o"]))