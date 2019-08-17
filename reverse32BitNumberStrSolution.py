class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
            
        def isNumberIn32Bitrange(x):
            if x < -2 **31 or x > (2 **31 -1):
                return False
            return True
        
        if isNumberIn32Bitrange(x):
            if x <0:
                x = x*-1
                number = -int(str(x)[::-1])
                if isNumberIn32Bitrange(number):
                    return number
                return 0
            number = int(str(x)[::-1])
            if isNumberIn32Bitrange(number):
                return number
            return 0
            
        return 0
