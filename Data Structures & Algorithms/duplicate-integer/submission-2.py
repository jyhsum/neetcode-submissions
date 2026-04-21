class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            if i in h:
                return True
            else:
                h[i] = True
        return False