class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        curr = []
        result = []

        def backtracking(open_p, close_p):
            if open_p > n:
                return
            if n == open_p and open_p == close_p:
                result.append("".join(curr)) 
                return
            
            if open_p < n:
                curr.append("(")
                backtracking(open_p + 1, close_p)
                curr.pop()
            if close_p < open_p:
                curr.append(")")
                backtracking(open_p, close_p + 1)
                curr.pop()

        backtracking(0, 0)
        return result
        