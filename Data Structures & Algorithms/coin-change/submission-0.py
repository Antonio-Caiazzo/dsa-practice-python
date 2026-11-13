class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        memo = {}

        def dfs(r):

            if r < 0:
                return float("inf")
            
            if r in memo:
                return memo[r]

            if r == 0:
                return 0
            
            res = float("inf")
            for coin in coins:
                res = min(res, 1 + dfs(r - coin))

            memo[r] = res
            return memo[r]


        return dfs(amount) if dfs(amount) != float("inf") else -1        