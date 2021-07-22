'''Problem statement: You are given a maze with N cells. Each cell may have multiple entry points but not more than one exit (ie. entry/exit points are unidirectional doors like valves). The cells are named with an integer value from 0 to N-1. You need to find the following:

Nearest meeting cell: Given any two cells - C1,C2, find the closest cell Cm that can be reached from both C1 and C2.

Note: Aim for O(Log(N)) solution.

INPUT FORMAT - First line has the number of cells N

Second line has list of N values of the edge[] array. edge[i] contains the cell number that can be reached from of cell ‘i’ in one step. edge[i] is - 1 if the 'i’th cell doesn’t have an exit.

Third line contains two cell numbers whose nearest meeting cell needs to be found. (return -1 if there is no meeting cell from the two given cells).

OUTPUT FORMAT - Find nearest meeting cell (NMC).'''


def nearestMeetingPoint(arr,src,dest):
    arr = [int(x) for x in arr.split()]
    c = [0]*len(arr)
    d = [0]*len(arr)
    c[src] = 1
    d[dest] = 1
    for i in range(len(arr)):
        if arr[src]!=-1:
            c[arr[src]] = 1
            if d[arr[src]]==1:
                return arr[src] 
            
            src = arr[src]
        
        if arr[dest]!=-1:
            if c[arr[dest]]==1:
                return arr[dest] 
            d[arr[dest]]=1
               
            dest = arr[dest]
nearestMeetingPoint("4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21", 2,9)
          
    