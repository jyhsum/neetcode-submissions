class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder_map = {0: -1}
        prefix_sum = 0
        for idx, num in enumerate(nums):
            prefix_sum += num
            rem = prefix_sum % k
            if rem in reminder_map:
                if idx - reminder_map[rem] >= 2:
                    return True
            else:
                reminder_map[rem] = idx
        return False

