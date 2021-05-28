# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        color = [0]*len(graph)
        def dfs(node, c):
            visited[node] = 1
            color[node] = c
            for i in graph[node]:
                if visited[i]==0:
                    if not dfs(i,c^1):
                        return False
                else:
                    if color[i]==color[node]:
                        return False
            return True
        for i in range(len(graph)):
            if visited[i]==0:
                if not dfs(i,0):
                    return False
        return True