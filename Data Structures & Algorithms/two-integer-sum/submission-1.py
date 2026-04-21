class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index, n in enumerate(nums):
            if target - n in h:
                return [h[target - n], index]
            h[n] = index

        