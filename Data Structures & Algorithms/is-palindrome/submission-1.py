class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for l in s :
            if l.isalnum() and l != ' ':
                t += l.lower()

        return t == t[::-1]