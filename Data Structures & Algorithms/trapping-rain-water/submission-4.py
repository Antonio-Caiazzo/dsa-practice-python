class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        total_water = 0

        while l < r:
            if max_left < max_right:
                total_water += 0 if max_left - height[l] <= 0 else max_left - height[l]
                l += 1
                max_left = max(height[l], max_left)
            else:
                total_water += 0 if max_right - height[r] <= 0 else max_right - height[r]
                r -= 1
                max_right = max(height[r], max_right)
        
        return total_water

        

        