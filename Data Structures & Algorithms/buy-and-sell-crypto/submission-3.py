class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minBuy = prices[0]
        
        for sell in prices:
            max_profit = max(sell - minBuy, max_profit)
            minBuy = min(minBuy, sell)
        return max_profit
