class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for idx, num in enumerate(nums):
            if zero_cnt > 0:
                if num != 0:
                    res[idx] = 0
                else:
                    res[idx] = prod
            else:
                res[idx] = prod // num
        return res