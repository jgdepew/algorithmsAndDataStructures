# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not len(prices) or len(prices) == 1:
        return 0
    
    buy = max(prices)
    profit = 0
    for i in range(0, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        if prices[i] - buy > 0:
            profit += prices[i] - buy
            buy = prices[i]
    return profit