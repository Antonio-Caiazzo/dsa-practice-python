class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        for b in s:
            if b in ")]}" and stack:
                if stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b) 
        
        return True if not stack else False
        