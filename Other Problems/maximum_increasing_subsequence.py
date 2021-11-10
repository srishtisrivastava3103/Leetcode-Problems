# Given an array, return the maximum increasing subsequence which has the greatest sum, along with the subsequence.
#Input: [10, 70, 20, 30, 50, 11, 30]
#Output: [110, [10, 20, 30, 50]]


def maxSumIncreasingSubsequence(array):
    # Write your code here.
    res = [float('inf')]
    ans = []
    flag=0
    for i in array:
        if i>0:
            flag = 1
    if flag==0:
        return [max(array),[max(array)]]
    def solve(res,n):
    #         print(res,n)
        if n==-1:
            ans.append(res[::-1])
            return 0
        elif array[n]<res[-1]:            
            return max(array[n]+solve(res+[array[n]],n-1),solve(res,n-1))
        else:
            return solve(res,n-1)

    s = solve(res,len(array)-1)
    print(ans)
    for i in ans:
        if sum(i[:-1])==s:
            return [s,i[:-1]]
