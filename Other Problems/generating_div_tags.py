# For a positive value n, generate all valid combinations <div> tags

def generateDivTags(numberOfTags):
    # Write your code here.
    res = []
    solve(0,0,numberOfTags,"",res)
    return res
def solve(open,close,n,string,res):
	if open==n and close==n:
		res.append(string)
		return True
	if open<n and open>0:
		if close<open:
			return solve(open+1,close,n,string+"<div>",res) and solve(open,close+1,n,string+"</div>",res)
		else:
			return solve(open+1,close,n,string+"<div>",res)
	elif open==0:
		return solve(open+1,close,n,string+"<div>",res)
	elif open==n and close<n: 
		return solve(open,close+1,n,string+"</div>",res)
		
	
