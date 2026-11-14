class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        profit = 0
        current_profit = 0
        for price in prices:
            if price >= lowest_price:
                current_profit = max(current_profit, price - lowest_price)
            else:
                profit = max(current_profit, profit)
                lowest_price = price
                current_profit = 0
        profit = max(current_profit, profit)
        return profit
            
        