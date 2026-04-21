class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, l = nums[0], 0
        i = 0

        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                l = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            
            l += 1
            curr += 1
            res = max(res, l)
        return res