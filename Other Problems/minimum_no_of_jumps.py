
def minNumberOfJumps(array):
    # Write your code here.
    def solve(step):
        if step>=len(array)-1:
            return 0
        ans = float('inf')

        for i in range(1,array[step]+1):
            temp = 1+solve(step+i)
            print(temp)
            ans = min(temp, ans)
        return ans
    return solve(0)
minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])

		
