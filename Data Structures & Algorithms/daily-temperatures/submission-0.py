from collections import deque 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for index, element in enumerate(temperatures):
            if not stack or element <= temperatures[stack[-1]]:
                stack.append(index)
                continue
            while stack and element > temperatures[stack[-1]]:
                output[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return output 