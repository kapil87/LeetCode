class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        keys = [0]
        while keys:
            next_key = keys.pop()
            for key in rooms[next_key]:
                if not visited[key]:
                    visited[key] = True
                    keys.append(key)
        return all(visited)
