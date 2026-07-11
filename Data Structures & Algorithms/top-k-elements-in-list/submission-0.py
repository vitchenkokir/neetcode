from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        new_cnt = dict(sorted(cnt.items(), key=lambda item: item[1], reverse=True))
        return list(new_cnt.keys())[:k]
        