class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for l in s :
            if l.isalnum() and l != ' ':
                t += l
        reversed_t = ''
        for c in t[::-1]:
            reversed_t += c
        return reversed_t.lower() == t.lower()