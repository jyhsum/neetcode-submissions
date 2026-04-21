class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0
        
        max_count = 0

        while l < len(s):
            count = 0
            tmp = {}
            r = l
            while r < len(s) and s[r] not in tmp:
                tmp[s[r]] = True
                r += 1
                count += 1

            l += 1
            max_count = max(count, max_count)
        
        return max_count

