class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        result = []
        curr = []

        def combine(index):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return
            
            for letter in letters[digits[index]]:
                curr.append(letter)
                combine(index + 1)
                curr.pop()
        combine(0)
        return result
        