class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def helper(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
            if remaining < 0:
                return 
            else:
                for i in range(start, len(nums)):
                    helper(i, path + [nums[i]], remaining-nums[i])
        helper(0, path, target)
        return res     