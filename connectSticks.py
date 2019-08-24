class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        total_min_cost = 0
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            total_min_cost += stick1 + stick2
            #print sticks
            heapq.heappush(sticks, (stick1 + stick2))
        return total_min_cost
