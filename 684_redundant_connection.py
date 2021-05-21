# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1]*(len(edges)+1)
        def findparent(i):
            if parent[i]==-1:
                return i
            else:
                return findparent(parent[i])
        def union(x,y):
            parent[x] = y
        for i in range(len(edges)):
            x = findparent(edges[i][0])
            y = findparent(edges[i][1])
            if x==y:
                return edges[i]
            union(x,y)
        return []
