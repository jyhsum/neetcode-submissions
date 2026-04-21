class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in h:
                h[sorted_s].append(s)
            else:
                h[sorted_s] = [s]
        return list(h.values())
