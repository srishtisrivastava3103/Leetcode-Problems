#https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def bfs(n):
            q = [[n[0],n[1],0]]
            t = 1
            visited = set()
            visited.add((q[0][0],q[0][1]))
            while q:
                i,j, d = q.pop(0) 
                if i-1>=0 and (i-1,j) not in visited:
                    if mat[i-1][j]==0:
                        return d+1
                    else:

                        q.append([i-1,j,d+1])
                        visited.add((i-1,j))

                if i+1<len(mat) and (i+1,j) not in visited:
                    if mat[i+1][j]==0:
                        return d+1
                    else:
                        q.append([i+1,j,d+1])
                        visited.add((i+1,j))

                if j-1>=0 and (i,j-1) not in visited:
                    if mat[i][j-1]==0:
                        return d+1
                    else:
                        q.append([i,j-1,d+1])
                        visited.add((i,j-1))

                if j+1<len(mat[0]) and (i,j+1) not in visited:
                    if mat[i][j+1]==0:
                        return d+1
                    else:
                        q.append([i,j+1,d+1])
                        visited.add((i,j+1))
            return len(mat)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
            
                if mat[i][j]==0:
                    mat[i][j] = 0
                else:
                    mat[i][j] = bfs([i,j])
        return mat
                    
                
                        