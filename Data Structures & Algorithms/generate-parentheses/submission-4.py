class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        currComb = []

        def backtracking(open_p, close_p):

            if n == open_p and open_p == close_p:
                result.append("".join(currComb))
                return

            if open_p < n:
                currComb.append("(")
                backtracking(open_p + 1, close_p)
                currComb.pop()
            if open_p > close_p:
                currComb.append(")")
                backtracking(open_p, close_p + 1)
                currComb.pop()

        backtracking(0, 0)
        return result
