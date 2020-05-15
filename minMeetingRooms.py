class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        rooms_in_heap = []
        
        intervals.sort(key= lambda interval: interval[0])
        
        heapq.heappush(rooms_in_heap, intervals[0][1])
        
        for i in intervals[1:]:
            if rooms_in_heap[0] <= i[0]:
                heapq.heappop(rooms_in_heap)
            
            heapq.heappush(rooms_in_heap, i[1])
        
        return len(rooms_in_heap)
