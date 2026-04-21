class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(path.copy())
                return
            if i >= len(nums) or total > target:
                return

            path.append(nums[i])
            backtrack(i, cur, total + nums[i])

            path.pop()
            backtrack(i + 1, cur, total)
        

        backtrack(0, [], 0)
        return res