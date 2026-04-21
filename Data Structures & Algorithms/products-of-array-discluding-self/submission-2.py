class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        elif zero_cnt == 1:
            output = [0] * len(nums)
            total = 1
            zero_idx = None
            for idx, val in enumerate(nums):
                if val != 0:
                    total *= val
                else:
                    zero_idx = idx
            output[zero_idx] = total
        else:
            output = []
            total = 1
            for idx, val in enumerate(nums):
                total *= val
            for j in nums:
                value = total // abs(j)
                if j < 0:
                    output.append(-value)
                else:
                    output.append(value)
        return output