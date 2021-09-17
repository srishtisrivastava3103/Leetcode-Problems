# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        l = intervals
        i = 1
        while i<len(l):
            if l[i-1][1]>=l[i][0]:
                l[i][0] = min(l[i-1][0],l[i][0])
                l[i][1] = max(l[i-1][1],l[i][1])
                l.pop(i-1)
            else:
                i+=1


        return l

        