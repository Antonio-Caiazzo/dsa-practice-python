class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True   

        parentheses = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            elif len(stack) > 0 and stack[-1] == parentheses[c]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


             