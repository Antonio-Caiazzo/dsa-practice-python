class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        resultComb, currComb = [], []

        def backtracking(open_brackets, close_brackets):

            if open_brackets == close_brackets and open_brackets == n:
                resultComb.append("".join(currComb))
                return

            
            if open_brackets < n:
                currComb.append("(")
                backtracking(open_brackets + 1, close_brackets)
                currComb.pop()

            if close_brackets < open_brackets:
                currComb.append(")")
                backtracking(open_brackets, close_brackets + 1)
                currComb.pop()
            else:
                return
        


        backtracking(0, 0)
        return resultComb
        