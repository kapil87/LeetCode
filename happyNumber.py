class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_list = []
        
        while True:
            square_sum = sum([int(x)**2 for x in str(n)])
            #print 'suqare_sum:', square_sum
            #print 'sum_list: ',sum_list
            if square_sum == 1:#Implies number is Happy
                return True
            if square_sum in sum_list:#Implied cycle
                return False 
            else:
                sum_list.append(square_sum)#Implies we have got new sum
            n = square_sum
