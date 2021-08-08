# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k==1:
            return 0
        parent = self.kthGrammar(n-1,k//2+k%2)
        if parent==1:
            if k%2==0:
                return 0
            else:
                return 1
        else:
            if k%2==0:
                return 1
            else:
                return 0

            