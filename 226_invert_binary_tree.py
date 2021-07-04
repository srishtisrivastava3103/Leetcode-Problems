#https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        q = [root]
        while q:
            node = q.pop(0)
            l = node.left
            r = node.right
            node.left = r
            node.right = l
            if node.left!=None:
                q.append(node.left)
            if node.right!=None:
                q.append(node.right)
        return root