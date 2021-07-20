# https://practice.geeksforgeeks.org/problems/sum-tree/1

class Solution:
    def isSumTree(self,root):
        # Code here
        def sum_(root):
            if root==None:
                return 0
            return sum_(root.left)+root.data+sum_(root.right)
            
        if root==None or (root.left==None and root.right==None):
            return 1
        ls = sum_(root.left)
        rs = sum_(root.right)
        if root.data==ls+rs:
            return 1
        else:
            return 0
