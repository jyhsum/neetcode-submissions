class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profix = 0
        min_buy = prices[0]

        for price in prices:
            max_profix = max(max_profix, price - min_buy)
            min_buy = min(min_buy, price)
        
        return max_profix