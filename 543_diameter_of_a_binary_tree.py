# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getOutermost(node):
            if not node:
                return 0
            left_dia = getOutermost(node.left)
            right_dia = getOutermost(node.right)
            self.ans = max(self.ans,left_dia+right_dia)
            return max(left_dia,right_dia)+1
        self.ans = 0
        getOutermost(root)
        return self.ans
