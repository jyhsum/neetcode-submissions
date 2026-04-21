class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_idx = {}
        for idx, val in enumerate(numbers):
            if (target-val) in nums_idx:
                return [nums_idx[target-val], idx + 1]

            nums_idx[val] = idx + 1
        
        return []
