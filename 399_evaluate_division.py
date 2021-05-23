# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        for i in range(len(equations)):

            if equations[i][0] in d:
                d[equations[i][0]].append((equations[i][1],values[i]))

            else:
                d[equations[i][0]] = [(equations[i][1],values[i])]

            if equations[i][1] in d:
                d[equations[i][1]].append((equations[i][0],1/values[i]))
            else:
                d[equations[i][1]]=[(equations[i][0],1/values[i])]

        def dfs(st, en, visited):
   
            if not(st in d and en in d):
                return -1
            if st==en:
                return 1
            visited.append(st)
            for i in d[st]:
                if i[0] in visited:
                    continue
                a = dfs(i[0],en,visited)
                if a!=-1:
                    return a*i[1]
            return -1
        ans = []
        for i in range(len(queries)):
            visited = []
            res = dfs(queries[i][0],queries[i][1],visited)
            ans.append(res)

        return ans
