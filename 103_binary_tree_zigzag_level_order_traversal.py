#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        q = [(root, 0)]
        ans = []
        prevht = -1
        while q:
            node, ht = q.pop(0)
            if prevht==ht:
                ans[-1].append(node.val)
            else:
                ans+=[[node.val]]
            prevht = ht
            if node.left:
                q.append((node.left,ht+1))
            if node.right:
                q.append((node.right, ht+1))
        for i in range(len(ans)):
            if i%2!=0:
                ans[i] = ans[i][::-1]
        return ans
        