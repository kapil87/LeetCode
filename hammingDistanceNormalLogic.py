class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        mask = 1
        BITS_IN_DIGIT = 32
        #Loop throough all bits
        for i in range(BITS_IN_DIGIT):
            if n & mask !=0:
                bits +=1
            #Shift mask 1 bit at a time
            mask <<=1
        return bits
