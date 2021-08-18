# https://leetcode.com/problems/maximum-population-year/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        l = list(range(1950,2051))
        d = dict.fromkeys(l,0)
        # print(d)
        for lt in logs:
            for j in range(lt[0],lt[1]):
                d[j]+=1
        return max(d,key = d.get)        

