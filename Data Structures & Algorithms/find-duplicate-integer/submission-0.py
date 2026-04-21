class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n - 1 # 代表數值, 不是index
        while low < high:
            mid = low + (high - low) // 2
            count = sum(1 for num in nums if num <= mid)

            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low