# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        color = [0]*(n+1)
        visited = [0]*(n+1)
        visited[0] = 1
        def dfs(node, c):
            visited[node] = 1
            color[node] = c
            for i in graph[node]:
                if visited[i]==0:
                    if not dfs(i,c^1):
                        return False
                else:
                    if color[node]==color[i]:
                        return False
            return True
        for i in range(n+1):
            if visited[i]==0:
                if not dfs(i, 0):
                    return False
        return True
        