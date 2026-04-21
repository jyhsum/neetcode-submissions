from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)

        for l in range(len(s2) - len(s1) + 1):
            if Counter(s2[l:l + len(s1)]) == s1_count:
                return True
        return False
            

            