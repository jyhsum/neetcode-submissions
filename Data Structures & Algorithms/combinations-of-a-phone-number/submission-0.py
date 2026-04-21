class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, cur_s):
            if len(cur_s) == len(digits):
                res.append(cur_s)
                return
            for c in digitToChar[digits[i]]:
                dfs(i + 1, cur_s + c)
        
        dfs(0, '')

        return res