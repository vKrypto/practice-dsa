# https://leetcode.com/problems/keys-and-rooms/

from .  import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        rooms_visited = [False]*n

        def dfs(node=0):
            rooms_visited[node] = True
            for child in rooms[node]:
                if not rooms_visited[child]:
                    dfs(child)

        dfs()
        return all(rooms_visited)