class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        diff = 0
        for price in prices:
            diff = max(diff, price - min_price)
            min_price = min(min_price, price)
        return diff