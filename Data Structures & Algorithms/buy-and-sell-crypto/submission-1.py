class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0
        l = 0

        for r in range(1, len(prices)):
            
            if prices[l] > prices[r]:
                l = r
            
            else:
                profit = prices[r] - prices[l]
                maximum_profit = max(maximum_profit, profit)
        
        return maximum_profit
        
    