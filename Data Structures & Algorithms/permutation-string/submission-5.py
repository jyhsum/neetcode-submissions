class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = {}
        for s in s1:
            count1[s] = count1.get(s, 0) + 1
        
        window_count = {}
        l = 0
        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1

            if count1 == window_count:
                return True
            
        return False

