# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n-1
        
        def helper(length,k):
            if k==1:
                return False
            pivot = length//2 +1
            if k==pivot:
                return True
            if k<pivot:
                return helper(pivot-1,k)
            if k>pivot:
                return not helper(pivot-1,2*pivot-k)
        
        return str(int(helper(length,k)))
        