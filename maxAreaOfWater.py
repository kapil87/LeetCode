class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        max_area = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                max_area = max(max_area, min(height[i], height[j])*(j-i))
        return max_area
        '''
        i, j = 0, len(height)-1
        max_water = 0
        while i < j:
            max_water = max(max_water, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i +=1
            else:
                j -=1
        return max_water
