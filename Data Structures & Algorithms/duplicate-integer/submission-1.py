class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicated = False
        tmp = {}
        for i in nums:
            if i in tmp:
                has_duplicated = True
            else:
                tmp[i] = i
        return has_duplicated