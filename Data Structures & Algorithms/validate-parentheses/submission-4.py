class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in closeToOpen:
                print(stack)
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True