class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def calculate(n):

            if n <= 1:
                memo[n] = 1
            
            if n not in memo:
                memo[n] = calculate(n - 1) + calculate(n - 2)

            return memo[n]
        
        return calculate(n)