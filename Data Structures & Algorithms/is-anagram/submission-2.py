class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_i = {}
        for i in s:
            if i not in count_i:
                count_i[i] = 1
            else:
                count_i[i] += 1

        count_j = {}
        for j in t:
            if j not in count_j:
                count_j[j] = 1
            else:
                count_j[j] += 1


        # for k in t:
        #     if k not in count_i:
        #         return False
        #     if count_j[k] != count_i[k]:
        #         return False   

        return count_j == count_i
        