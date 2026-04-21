class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, target):
            l, r = 0 , len(nums) - 1
            while l <= r:
                mid = l + ((r - l) // 2)
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1

        expand_list = []
        for m in matrix:
            expand_list.extend(m)
        print(expand_list)
        res = binary_search(expand_list, target)
        if res > -1:
            return True
        return False



        