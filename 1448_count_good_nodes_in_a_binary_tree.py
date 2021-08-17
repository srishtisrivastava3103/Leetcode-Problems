# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = []
        def dfs(n,path,visited):
            # print(path)
            # print(n.val)
            if path and max(path)<=n.val:
                ans.append(n.val)                
            visited.add(n)
            for i in [n.left,n.right]:
                if i and i not in visited:
                    dfs(i,path+[i.val],visited)
        dfs(root,[root.val], set() )
        # print(ans)
        return len(ans)
            
                    
            
        