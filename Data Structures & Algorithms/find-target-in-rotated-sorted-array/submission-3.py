class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        minium_idx = l

        if target < nums[0]:
            l, r = minium_idx, len(nums) - 1
        elif minium_idx == 0:
            l, r = 0, len(nums) - 1
        else:
            l, r = 0, minium_idx - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

