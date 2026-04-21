class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, val in enumerate(numbers):
            match_idx = self.binary_search(target - val, numbers)
            if match_idx:
                return [idx + 1, match_idx + 1]

    def binary_search(self, target, numbers):
        l, r = 0, len(numbers) - 1
        while l <= r:
            mid = (l + r) // 2
            if numbers[mid] < target:
                l = mid + 1
            elif numbers[mid] > target:
                r = mid - 1
            else:
                return mid
        return None
