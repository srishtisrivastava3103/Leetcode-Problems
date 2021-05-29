# Cycle Detection using back edge in DFS

def cycledetection(graph = [[1],[0,2,3],[1,3],[1,4,2],[3]]):
    visited = [0]*5
    def dfs(node,parent):
        visited[node]=1
        for i in graph[node]:
            if visited[i]==0:
                if dfs(i, node)==True:
                    return True
            else:
                if parent!=i:
                    return True
        return False
    return dfs(0, 0)
cycledetection()