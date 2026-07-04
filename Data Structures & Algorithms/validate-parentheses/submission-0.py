class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for b in s:
            if b in "([{":
                stack.append(b)
            elif b in brackets:
                if not stack or brackets[b] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0
        