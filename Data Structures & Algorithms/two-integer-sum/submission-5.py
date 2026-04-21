class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, n in enumerate(nums):
            rest = target - n
            if rest in h:
                return [h[rest], idx]
            else:
                h[n] = idx

