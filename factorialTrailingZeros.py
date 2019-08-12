class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        DIVISION_NUMBER = 5
        count = 0
        '''
        // is the floored-division operator in Python
        # Python 2
          >>> 10.0 / 3
          3.3333333333333335
          >>> 10.0 // 3
          3.0
        '''
        while n >0:
            count += n//DIVISION_NUMBER
            n //=DIVISION_NUMBER
        return count
            
        
