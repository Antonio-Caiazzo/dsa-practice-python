class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0
        l = 0

        for r in range(len(prices)):
            
            while prices[l] > prices[r]:
                l += 1
            
            profit = prices[r] - prices[l]
            maximum_profit = max(maximum_profit, profit)
        
        return maximum_profit
        
    