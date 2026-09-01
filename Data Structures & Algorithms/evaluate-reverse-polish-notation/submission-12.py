class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                res = int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif token == '*':
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)
            elif token == '-':
                res = -int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif token == '/':
                res = int((1/int(stack.pop()) * int(stack.pop())))
                stack.append(res)
            else:
                stack.append(int(token))

        return int(stack.pop())