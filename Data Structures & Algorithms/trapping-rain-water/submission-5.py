class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        total_water = 0

        while l < r:
            if max_left < max_right:
                total_water += max_left - height[l]
                l += 1
                max_left = max(height[l], max_left)
            else:
                total_water +=  max_right - height[r]
                r -= 1
                max_right = max(height[r], max_right)
        
        return total_water

        

        