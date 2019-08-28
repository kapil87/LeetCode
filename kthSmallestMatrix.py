#https://medium.com/brain-framework/kth-smallest-element-in-sorted-matrix-b20400cf878e
#Heap Solution
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for row in matrix:
            for num in row:
                heapq.heappush(heap, -1*num)
                
                if len(heap) > k:
                    heapq.heappop(heap)
                    
        return -1*heapq.heappop(heap)
        
