# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        def dfs(node):
            if node not in visited:
                new = Node(node.val)
                visited[node] = new
                for i in node.neighbors:
                    new.neighbors.append(dfs(i))
                return new
            else:
                return visited[node]
        clone = dfs(node)
        return clone
                    
                    