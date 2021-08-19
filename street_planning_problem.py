# https://codereview.stackexchange.com/questions/118966/solution-to-king-kohima-problem-in-python

def streetPlan(n):
    ans = []
    def solve(n,prev):
        if n==0:
            ans.append(prev)
            return 1
        if prev[-1]=="X":
            return solve(n-1,prev+"Y")
        else:
            return solve(n-1,prev+"X") and solve(n-1,prev+"Y")

    solve(n-1,"Y") 
    print(ans)
    solve(n-1,"X")
    print(ans)
    return len(ans)**2
streetPlan(3)