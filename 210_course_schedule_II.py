# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = [[] for i in range(numCourses)]
        for i,j in prerequisites:
            pre[i].append(j)
        visited = [0]*numCourses
        ans = []
        def dfs(node, visited, ans, pre):
            if visited[node]==1:
                return False
            if pre[node]==[]:
                if node not in ans:
                    ans.append(node)
                return True
            visited[node] = 1
            for i in pre[node]:
                if not dfs(i,visited, ans, pre):
                    return False
            visited[node] = 0
            if node not in ans:
                ans.append(node)
            pre[node] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i, visited, ans, pre):
                return []
        return ans
        