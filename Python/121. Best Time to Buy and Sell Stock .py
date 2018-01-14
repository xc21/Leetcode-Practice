class Solution(object):
    def maxprofit(selfself,prices):
        if len(prices)< 2:
            return 0 #only can buy not be able to sell
        min_price =  prices[0]
        max_profit = 0
        for price in prices:
            if price <- min_price:
                min_price<- price
            if price-min_price > max_profit:
                max_profit <- price-min_price
        return max_profit

        
