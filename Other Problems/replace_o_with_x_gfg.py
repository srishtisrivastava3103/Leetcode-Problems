#https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1

def floodfill(n,m,mat):
    for i in range(n):
        for j in range(m):
            if mat[i][j]=="O":
                mat[i][j] = "-"
    def boundaryfill(i,j,mat):
        if mat[i][j]=="X":
            return
        if i-1>=0 and mat[i-1][j]=="-":
            mat[i-1][j] = "O"
            boundaryfill(i-1,j,mat)
        if i+1<len(mat) and mat[i+1][j]=="-":
            mat[i+1][j] = "O"
            boundaryfill(i+1,j,mat)
        if j-1>=0 and mat[i][j-1]=="-":
            mat[i][j-1] = "O"
            boundaryfill(i,j-1,mat)
        if j+1<len(mat[0]) and mat[i][j+1]=="-":
            mat[i][j+1] = "O"
            boundaryfill(i,j+1,mat)

    for i in range(0,m):
        if mat[0][i]=="-":
            mat[0][i] = "O"
            boundaryfill(0,i,mat)
        if mat[n-1][i]=="-":
            mat[n-1][i] = "O"
            boundaryfill(n-1,i,mat)
    for i in range(0,n):
        if mat[i][0]=="-":
            mat[i][0] = "O"
            boundaryfill(i,0,mat)
        if mat[i][m-1]=="-":
            mat[i][m-1] = "O"
            boundaryfill(i,m-1,mat)
    for i in range(n):
        for j in range(m):
            if mat[i][j]=="-":
                mat[i][j] = "X"
    return mat
