class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        l = 0


        for r in range(len(prices)):

            if prices[l] > prices[r]:
                l = r

            maximumProfit = max(maximumProfit, prices[r] - prices[l])

        return maximumProfit
