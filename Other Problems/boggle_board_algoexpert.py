def boggleBoard(board, words):
    # Write your code here.
    ans = []

    def dfs(i,j,word,char):
        if char==len(word)-1:
            return True
        
        visited.add((i,j))
        left = [i,j-1]
        right = [i, j+1]
        up = [i-1,j]
        down = [i+1,j]
        right_diag = [i+1,j+1]
        left_diag = [i+1,j-1]
        upper_right_diag = [i-1,j+1]
        upper_left_diag = [i-1,j-1]
        
        for row,col in [left,right,up,down,right_diag,left_diag,upper_right_diag,upper_left_diag]:
            if 0<=row<len(board) and 0<=col<len(board[0]) and word[char+1]==board[row][col] and (row,col) not in visited:
                print(board[row][col])
                if dfs(row,col,word,char+1):
                    return True
        visited.remove((i,j))
        return False

    for word in words:
        f = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited = set()
                    if dfs(i,j,word,0):
                        f = 1
                        break
            if f==1:
                ans.append(word)
                break
    return ans

        
        
                
			
