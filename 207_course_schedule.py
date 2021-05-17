# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            pre[prerequisites[i][0]].append(prerequisites[i][1])
        visited = set()
        def dfs(node, visited, pre):
            if node in visited:
                return False
            if pre[node] == []:
                return True
            visited.add(node)
            for i in pre[node]:
                if not dfs(i,visited, pre):
                    return False
            visited.remove(node)
            pre[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i,visited,pre ):
                return False
        return True
        