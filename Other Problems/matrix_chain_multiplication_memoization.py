# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1]*(N+1) for i in range(N+1)]
        def mcm(arr,i,j):
            if i>=j:
                return 0
            if dp[i][j]!=-1:
                ans = dp[i][j]
                return ans
            ans = float('inf')
            for k in range(i,j):
                ans = min(ans,mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j])
            dp[i][j] = ans
            return ans
        return mcm(arr,1,N-1)
