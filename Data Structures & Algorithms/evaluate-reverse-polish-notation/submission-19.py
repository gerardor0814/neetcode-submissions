class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opset = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token not in opset:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(right + left)
                if token == '-':
                    stack.append(left - right)
                if token == '*':
                    stack.append(left * right)
                if token == '/':
                    stack.append(int(left / right))
        return stack.pop()