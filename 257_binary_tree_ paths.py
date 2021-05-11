# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        if root==None:
            return []
        def dfs(root, path, paths):
            path+=str(root.val)
            if root.left==None and root.right==None:
                paths.append(path)
                return 
            if root.left:
                dfs(root.left,path+"->",paths)
            if root.right:
                dfs(root.right,path+"->", paths)

        dfs(root,"",paths)
        return paths


    