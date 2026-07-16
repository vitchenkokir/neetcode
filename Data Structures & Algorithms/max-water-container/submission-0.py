class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        l, r = 0, len(heights) - 1
        while l < r:
            extent = min(heights[l], heights[r]) * (r - l)
            mx = max(extent, mx)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return mx