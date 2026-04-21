class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, cur in enumerate(nums):
            if cur > 0:
                break
            if idx > 0 and cur == nums[idx - 1]:
                continue

            l = idx + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + cur
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([cur, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        return res
                    
