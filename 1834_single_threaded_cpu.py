# https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i,t in enumerate(tasks):
            t.append(i)
        tasks = sorted(tasks,key = lambda x:x[0])
        i = 0
        time = tasks[0][0]
        ans = []
        heap = []
        while i<len(tasks) or heap:
            while i<len(tasks) and  time>=tasks[i][0]:
                if tasks[i][0]<=time:
                    heapq.heappush(heap,[tasks[i][1],tasks[i][2]])
                    i+=1

            if heap:
                end,ind = heapq.heappop(heap)
                ans.append(ind)
                time = time+end
            else:
                time = tasks[i][0]
        return ans

        
    