# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        s = sum(dist)
        if len(dist)-hour>1:
            return -1
        def check(dist,i):
            t = 0
            for j in range(len(dist)):
                if j!=len(dist)-1:
                    t+=math.ceil(dist[j]/i)
                else:
                    t+=dist[j]/i
            if t<=hour:
                return True
            else:
                return False

        low = max(int(sum(dist)//hour),1)
        high = 10**7
        while low<high:
            mid = low+(high-low)//2
            if check(dist, mid):
                high = mid
            else:
                low = mid+1

        if check(dist,high):
            return high
        else:
            return -1