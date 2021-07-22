'''You are given a maze with N cells. Each cell may have multiple entry points but not more than one exit (ie. entry/exit points are unidirectional doors like valves).

The cells are named with an integer value from 0 to N-1.

You need to find the the length of the largest cycle in the maze. Return -1 if there are no cycles.

INPUT FORMAT

First line has the number of cells N
Second line has list of N values of the edge[] array. edge[i] contains the cell number that can be reached from of cell ‘i’ in one step. edge[i] is -1 if the ‘i’th cell doesn’t have an exit.
OUTPUT FORMAT

length of the largest cycle.
Sample input:

23

4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21

Sample output

43'''


def largestsumcycle(arr):
    s = 0
    arr = [int(x) for x in arr.split()]
    visited = [0]*len(arr)

    for i in range(len(arr)):
        st = i
        j = arr[st]
        cs = 0
        visited[st] = 1

        while j!=-1 and not visited[j]:
            visited[j] = 1
            cs+=arr[j]
            j = arr[j]
            print(arr[j])
        s= max(s,cs)

        
    print(s)

largestsumcycle("4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21")
        
        
    