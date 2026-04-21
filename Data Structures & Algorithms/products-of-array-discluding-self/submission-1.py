class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        
        arr = []
        while i < len(nums):
            total = 1
            for j in range(len(nums)):
                if j == i:
                    pass
                else:
                    total *= nums[j]
            arr.append(total)
            i += 1
        return arr