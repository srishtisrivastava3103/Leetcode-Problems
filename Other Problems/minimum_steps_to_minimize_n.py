# https://practice.geeksforgeeks.org/problems/minimum-steps-to-minimize-n-as-per-given-condition0618/1

class Solution:
	def minSteps(self, N):
		if N==1:
		    return 0
        if N==2 or N==3:
            return 1
        l = [0]+list(range(0,N))
        l[2] = 1
        l[3] = 1

        for i in range(4,len(l)):
            one = two = float('inf')
            if i%2==0:
                one = l[i//2]+1
            if i%3==0:
                two = l[i//3]+1
            three = l[i-1]+1
            l[i] = min(one,two,three)
        return l[-1]
            