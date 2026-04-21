class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (r + l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)
            if total_time > h:
                l = k + 1
            else:
                r = k - 1
                res = min(res, k)
        return res
