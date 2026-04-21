class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        ana_hash = {}

        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in ana_hash:
                ana_hash[sorted_i].append(i)
            else:
                ana_hash[sorted_i] = [i]
        
        return list(ana_hash.values())