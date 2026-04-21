class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        arr = []

        while i < len(nums):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    pass
                else:
                    product *= nums[j]
            arr.append(product)
            i += 1
        return arr

