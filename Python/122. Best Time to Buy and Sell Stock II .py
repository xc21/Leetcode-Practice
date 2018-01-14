class Solution(object):
    def maxprofit(self,prices):
        if not prices:
            return 0
        max_price=min_price=prices[0]
        max_profit=0
        for price in prices:
            if price[prices]>=prices[price-1]:
                max_price = price[prices]
            else:
                max_profit += max_price-min_price #profit could be accumulated from last transaction
                min_profit=max_profit=price[prices]
            max_profit += max_price - min_price
        return max_profit
