# https://leetcode.com/problems/maximum-population-year/


#Method - 1: Brute Force

# class Solution:
#     def maximumPopulation(self, logs: List[List[int]]) -> int:
#         l = list(range(1950,2051))
#         d = dict.fromkeys(l,0)
#         # print(d)
#         for lt in logs:
#             for j in range(lt[0],lt[1]):
#                 d[j]+=1
#         return max(d,key = d.get)        

# Method-2
# Prefix Sum

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        l = list(range(1950,2051))
        d = dict.fromkeys(l,0)
        # print(d)
        for lt in logs:
            d[lt[0]]+=1
            d[lt[1]]-=1
        maxyear = 1950
        for i in range(1951,2051):
            d[i] +=d[i-1] 
            if d[i]>d[maxyear]:
                maxyear = i
        return maxyear
