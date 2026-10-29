class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            
            prev1, prev2 = min(prev1 + cost[i], prev2 + cost[i]), prev1

        return min(prev1, prev2)