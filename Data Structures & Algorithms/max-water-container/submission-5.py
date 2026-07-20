class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        l, r = 0, len(h) - 1
        res = 0
        while l < r:
            res = max(res, min(h[r], h[l]) * (r - l))
            if h[r] > h[l]:
                l += 1
            else:
                r -= 1
        return res
