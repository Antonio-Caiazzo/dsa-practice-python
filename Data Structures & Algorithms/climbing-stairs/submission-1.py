class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def calculate(n):

            if 0 <=n <= 2:
                return n

            if n in memo: return memo[n]

            memo[n] = calculate(n - 1) + calculate(n - 2)

            return memo[n]
        
        return calculate(n)