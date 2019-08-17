class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <2:
            return x
        
        left, right = 2, x//2
        
        while left <=right:
            mid = left + (right-left)//2
            square = mid * mid
            if square > x:
                right = mid -1
            elif square < x:
                left = mid+1
            else:
                return mid
        
        return right 
    
