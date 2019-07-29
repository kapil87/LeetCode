class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb_stairs(0, n)
    
    def climb_stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        #Climb stairs 1 step or 2 steps at a time.
        return self.climb_stairs(i+1, n) + self.climb_stairs(i+2, n)
