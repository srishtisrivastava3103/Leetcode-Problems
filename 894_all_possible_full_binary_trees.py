# https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {1:[TreeNode()]}
        def FBT(n):
            ans = []
            if n==1:  
                return [TreeNode()]

            for i in range(1,n,2):
                if i in dp.keys():
                    leftsub = dp[i]
                else:

                    leftsub = FBT(i)
                if n-i-1 in dp.keys():
                    rightsub = dp[n-i-1]
                else:
                    rightsub = FBT(n-1-i)


                for j in range(len(leftsub)):
                    for k in range(len(rightsub)):
                        root = TreeNode()
                        root.left = leftsub[j]
                        root.right = rightsub[k]
                        # print("HEre")
                        ans.append(root)
                    # print(ans)
            dp[n] = ans
            return  dp[n] 
        return FBT(n)