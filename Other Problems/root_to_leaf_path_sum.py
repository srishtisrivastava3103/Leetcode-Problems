# https://practice.geeksforgeeks.org/problems/root-to-leaf-path-sum/1#

def hasPathSum(self,root, S):
    '''
    :param root: root of given tree.
    :param sm: root to leaf sum
    :return: true or false
    '''
    # code here
    def dfs(root,s):
        if root==None:
            if s==S:
                return 1
            else:
                return 0
        if dfs(root.left,s+root.data) or dfs(root.right,s+root.data):
            return 1
    return dfs(root,0)
            
            
            