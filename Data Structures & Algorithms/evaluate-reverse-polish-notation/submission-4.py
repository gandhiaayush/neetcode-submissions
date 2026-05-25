class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda y, x: y + x,
            '-': lambda y, x: y - x,
            '*': lambda y, x: y * x,
            '/': lambda y, x: int(y / x),  # truncates toward zero
        }

        for element in tokens:
            if element in ops:
                x, y = stack.pop(), stack.pop()
                stack.append(ops[element](y, x))
            else:
                stack.append(int(element))

        return stack[0]