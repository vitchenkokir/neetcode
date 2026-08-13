class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        summ = []
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
            if remaining < 0:
                return
            else:
                for i in range(start, len(nums)):
                    backtrack(i, path + [nums[i]], remaining-nums[i])
        backtrack(0, summ, target)
        return res