class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_h = {}
        t_h = {}

        for i in range(len(s)):
            s_h[s[i]] = s_h.get(s[i], 0) + 1
            t_h[t[i]] = t_h.get(t[i], 0) + 1
        
        return s_h == t_h