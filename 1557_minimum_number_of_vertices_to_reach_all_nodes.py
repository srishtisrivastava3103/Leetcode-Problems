class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = [0]*n
        ans = []
        for i in range(len(edges)):
            inDegree[edges[i][1]]+=1
        for i in range(len(inDegree)):
            if inDegree[i]==0:
                ans.append(i)
        return ans
                
        