import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #we need to find max(prices[j] - prices[i])max(prices[j]−prices[i]), for every ii and jj such that j > ij>i.
        minprice = sys.maxsize
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif (price - minprice) > maxprofit:
                maxprofit = price - minprice
        return maxprofit
