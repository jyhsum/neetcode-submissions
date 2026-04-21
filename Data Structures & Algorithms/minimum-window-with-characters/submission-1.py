from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        missing = len(t)
        l = 0
        best_start, best_len = 0, float('inf')

        for r, c in enumerate(s):
            if needed[c] > 0:
                missing -= 1
            needed[c] -= 1

            while missing == 0:
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = l
                
                needed[s[l]] += 1
                if needed[s[l]] > 0:
                    missing += 1
                l += 1
        
        if best_len == float('inf'):
            return ""
        return s[best_start:best_start + best_len]
