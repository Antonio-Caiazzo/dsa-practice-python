class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = float("-inf")
        l = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                maximum_profit = max(maximum_profit, prices[r] - prices[l])

        return maximum_profit        

