# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        g = collections.defaultdict(list)
        for u,v in connections:
            g[u].append(v)
            g[v].append(u)
        def dfs(node, visited):
            visited[node] = 1
            for i in g[node]:
                if visited[i]==0:
                    dfs(i, visited)
        visited = [0]*n
        c = 0
        for i in range(len(visited)):
            if not visited[i]:
                dfs(i, visited)
                c+=1
        return c-1
        