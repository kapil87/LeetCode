def calculate(prices, s):
    if s >= len(prices):
        #print 's', s
        return 0

    maxProfitSoFar = 0
    #print 'maxProfitSoFar', maxProfitSoFar
    for start in range(s, len(prices)):
        maxProfit = 0
        #print 'maxProfit', maxProfit
        for i in range(start+1, len(prices)):
            if prices[start] < prices[i]:
                profit = calculate(prices, i+1) + prices[i] - prices[start]
                if profit > maxProfit:
                    print 'start: %s, i: %s'%(start, i)
                    maxProfit = profit
        if maxProfit > maxProfitSoFar:
            maxProfitSoFar = maxProfit
            print 'start: %s maxProfitSoFar: %s'%(start, maxProfitSoFar)

    return maxProfitSoFar

return calculate(prices, 0)
