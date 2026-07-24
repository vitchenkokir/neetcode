class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        res = 0
        l, r = 0, len(h) - 1
        while l < r:
            res = max(min(h[r], h[l]) * (r - l), res)
            if h[r] > h[l]:
                l += 1
            else:
                r -= 1
        return res