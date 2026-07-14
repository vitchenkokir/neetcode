class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = set(nums)
        max_len = 1
        for num in st:
            if num - 1 not in st:
                length = 1
                while num + 1 in st:
                    length += 1
                    num += 1
                max_len = max(length, max_len)
        return max_len