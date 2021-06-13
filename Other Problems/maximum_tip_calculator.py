# https://practice.geeksforgeeks.org/problems/maximum-tip-calculator2631/1

class Solution:
    def maxTip(self, a, b, n, x, y):
        
        # code here
        d = []
        for i in range(n):
            d.append([abs(a[i]-b[i]),i])
        d = sorted(d, key = lambda x:x[0], reverse = True)
        c = 0
        for i in range(n):
            if a[d[i][1]]>=b[d[i][1]]:
                if x>0:
                    x-=1
                    c+=a[d[i][1]]
                elif y>0:
                    y-=1
                    c+=b[d[i][1]]
            else:
                if y>0:
                    y-=1
                    c+=b[d[i][1]]
                elif x>0:
                    x-=1
                    c+=a[d[i][1]]
        return c
#{ 
#  Driver Code Starts
#Initial Template for Python 3







if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x, y = list(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ans = Solution().maxTip(a, b, n, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends