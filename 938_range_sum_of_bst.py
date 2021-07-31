# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if low<=root.val<=high:
                return root.val+ self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
            elif root.val<low:
                return 0+ self.rangeSumBST(root.right,low,high)  
            else:
                return 0+ self.rangeSumBST(root.left,low,high)
        return 0


            