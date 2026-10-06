class Solution:
    def isValid(self, s: str) -> bool:
        openpar = {'(', '{', '['}
        stack = []
        for c in s:
            if c in openpar:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ')' and stack.pop() != '(':
                        return False
                if c == '}' and stack.pop() != '{':
                    return False
                if c == ']' and stack.pop() != '[':
                    return False
        if stack:
            return False
        return True

            