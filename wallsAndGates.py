class Solution:
    
    def __init__(self):
        self.EMPTY = 2147483647
        self.GATE = 0
        self.WALL = -1
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for row in range(0, len(rooms)):
            for col in range(0, len(rooms[row])):
                if rooms[row][col] == self.EMPTY:
                    rooms[row][col] = self.distanceToNearestGate(rooms, row, col)
        return
        
    def distanceToNearestGate(self, rooms, startRow, startCol):
        distance = [[0 for _ in range(len(rooms[0]))] for _ in range(len(rooms))]
        queue = deque([(startRow, startCol)])
        min_distance = self.EMPTY
        while queue:
            row,col = queue.pop()
            for dirRow, dirCol in self.DIRECTIONS:
                r = row + dirRow
                c = col + dirCol
                if (r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]) or rooms[r][c] == self.WALL or distance[r][c] != 0):
                    continue
                
                #Add +1 to the neighbor and check for the gate
                print(distance)
                distance[r][c] = distance[row][col] + 1
                if rooms[r][c] == self.GATE:
                    if min_distance > distance[r][c]:
                        min_distance = distance[r][c]
                
                #Add neighbors to the queue
                queue.append((r,c))
        return min_distance
    
    
# Optimized solution for the same problem  
class Solution:
    
    def __init__(self):
        self.EMPTY = 2147483647
        self.GATE = 0
        self.DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0: return 
        m = len(rooms)
        n = len(rooms[0])
        queue = deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == self.GATE:
                    queue.append((r,c))

        while queue:
            row, col = queue.popleft()
            for dirRow, dirCol in self.DIRECTIONS:
                r = row + dirRow
                c = col + dirCol
                if (r < 0 or  c < 0 or r >= m or c >= n or rooms[r][c] != self.EMPTY):
                    continue
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r,c))
        #print(rooms)
    
