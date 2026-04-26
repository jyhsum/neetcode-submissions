class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            if nums[idx] + nums[idx + 1] + nums[idx + 2] > 0:
                break
            if nums[idx] + nums[len(nums) - 2] + nums[len(nums) - 1] < 0:
                continue

            while l < r:
                threeSum = nums[idx] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[idx], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l] : l += 1
                    while l < r and nums[r - 1] == nums[r]: r -= 1
                    l += 1
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return res