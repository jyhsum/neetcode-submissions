class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(sub_s):
            return sub_s == sub_s[::-1]
    
        def dfs(i):
            if i >= len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                sub_s = s[i:j+1]

                if is_palindrome(sub_s):
                    path.append(sub_s)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res
            