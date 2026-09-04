class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        currComb = []

        def backtracking(i):

            if i == len(s):
                result.append(currComb.copy())
                return

            for j in range(i, len(s)):
                new_string = s[i:j + 1]
                if new_string != new_string[::-1]:
                    continue
                currComb.append(new_string)
                backtracking(j + 1)
                currComb.pop()


        backtracking(0)
        return result