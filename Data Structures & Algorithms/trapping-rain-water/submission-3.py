class Solution:
    def trap(self, height: List[int]) -> int:        
        
        n = len(height)

        max_l = [0] * n
        max_r = [0] * n

        water = 0

        current_maximum = 0
        for i in range(n):
            current_maximum = max(current_maximum, height[i])
            max_l[i] = current_maximum 
        
        current_maximum = 0
        for i in range(n - 1, -1, -1):
            current_maximum = max(current_maximum, height[i])
            max_r[i] = current_maximum

        for i in range(n):
            minimum_value = min(max_l[i], max_r[i])
            water += minimum_value - height[i]

        return water

        
