class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < min_price:
                min_price = prices[r]
                l = r
                r += 1
                continue
            profit = max(profit, prices[r] - prices[l])
            r += 1
        return profit