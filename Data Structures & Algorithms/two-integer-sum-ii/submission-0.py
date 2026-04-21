class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        nums_idx = {}
        for idx, val in enumerate(numbers):
            nums_idx[val] = idx + 1
        
        for n in numbers:
            if (target-n) in nums_idx:
                output.append(nums_idx[n])
                output.append(nums_idx[target-n])
                output.sort()
                return output
        
        return output
