# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms)<=1:
            return True
        visited = [0]*len(rooms)
        def dfs(room,visited):
            if visited[room]==0:
                visited[room] = 1
                for i in rooms[room]:
                    dfs(i,visited)
        dfs(0, visited)
        if 0 in visited:
            return False
        else:
            return True