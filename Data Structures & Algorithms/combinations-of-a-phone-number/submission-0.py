class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        currComb, resultComb = [], []
        maps = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtracking(i):
            if len(currComb) == len(digits):
                resultComb.append("".join(currComb))
                return
            
            currDigit = digits[i]
            for letter in maps[currDigit]:
                currComb.append(letter)
                backtracking(i + 1)
                currComb.pop()

        backtracking(0)
        return resultComb
        