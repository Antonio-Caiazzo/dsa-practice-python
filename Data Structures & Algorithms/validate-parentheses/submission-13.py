class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for b in s:
            if b in "([{":
                stack.append(b)
            else:
                if len(stack) <= 0 or stack.pop() != brackets[b]:
                    return False

        return len(stack) == 0
        