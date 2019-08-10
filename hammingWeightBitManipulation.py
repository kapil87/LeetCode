class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        sum = 0
        while n:
            sum+=1
            # n & n-1 sets the LSB 1 to 0
            n &=(n-1)
        return sum
        
   #Following is pythonic solution
   def hammigWeightPythonic(self, n):
       return bin(n).count('1')
       
