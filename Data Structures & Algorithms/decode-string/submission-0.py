class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        number = ""
        string = ""
        for c in s:
            if c in "0123456789":
                number += c
            elif c == "[":
                stack.append((int(number), string))
                string = ""
                number = ""
            elif c == "]":
                count, strings = stack.pop()
                string = strings + (count * string)
            else:
                string += c
        return string
             