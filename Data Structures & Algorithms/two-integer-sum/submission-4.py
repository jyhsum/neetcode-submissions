class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in h:
                return [h[diff], idx]
            else:
                h[val] = idx
        
        return