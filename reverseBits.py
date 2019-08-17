class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        '''
        You can get the bits using format function as well
        >>> bits = '{0:032b}'.format(3)
        >>> bits
        '00000000000000000000000000000011'
        
        >>> bin(3)
        '0b11'
        >>>
        As bin returns 0b as prefix and all 0's are not shown we use zfill function.
        '''
        bits = bin(n)[2:].zfill(32)
        bits = bits[::-1]
        return int(bits, 2)
