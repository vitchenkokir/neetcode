class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for price in prices:
            res = max(res, price - min_price)
            min_price = min(min_price, price)
        return res
        
