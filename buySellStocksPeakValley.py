def maxProit(prices):
    i = 0
    maxprofit = 0
    while i < (len(prices) -1):
        while (i < len(prices)-1 and prices[i] >= prices[i+1]):
            i +=1
        valley = prices[i]
        while (i < len(prices)-1 and prices[i] <= prices[i+1]):
            i +=1
        peak = prices[i]
        #print peak, valley
        maxprofit += peak-valley
    return maxprofit
