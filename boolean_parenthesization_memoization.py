# https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/


dp = [[[-1,-1] for i in range (7)] for j in range(7)]
def boolParenthesization(s,i,j,isTrue):
    if i>j:
        return False
    if i==j:
        if isTrue==True and s[i]=="T":
                return True
        elif isTrue==False and s[i]=="F":
            return True
        else:
            return False
    
    ans = 0
    for k in range(i+1,j,2):
        if dp[i][k-1][1]!=-1:
            lT = dp[i][k-1][1]
        else:
            lT = boolParenthesization(s,i,k-1,True)
        if dp[k+1][j][1]!=-1:
            rT = dp[k+1][j][1]
        else:
            rT = boolParenthesization(s,k+1,j,True)
        if dp[i][k-1][0]!=-1:
            lF = dp[i][k-1][0]
        else:
            lF = boolParenthesization(s,i,k-1,False)
        if dp[k+1][j][0]!=-1:
            rF = dp[k+1][j][0]
        else:
            rF = boolParenthesization(s,k+1,j,False)

        if s[k]=="&":
            if isTrue:
                ans += lT*rT
            else:
                ans += lT*rF + lF*rT + lF*rF
        elif s[k]=="|":
            if isTrue:
                ans += lT*rT + lT*rF + lF*rT 
            else:
                ans += lF*rF
        else:
            if isTrue: 
                ans += lT*rF + lF*rT + lF*rF
            else:
                ans += lT*rT
    dp[i][j][isTrue] = ans
    return ans
boolParenthesization("T|T&F^T",0,6,True)

                
    
    