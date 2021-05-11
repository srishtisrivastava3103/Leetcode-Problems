# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        min_ = None
        max_ = None

        def helper(root, min_,max_):
            if root==None:
                return True
            elif (max_!=None and root.val>=max_) or (min_!=None and root.val<=min_):
                print(min_,max_)
                return False
            else:
                return helper(root.left,min_, root.val) and helper(root.right, root.val, max_)
        return helper(root, min_, max_)