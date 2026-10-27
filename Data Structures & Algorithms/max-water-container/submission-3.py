class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumWater = 0
        l, r = 0, len(heights) - 1

        while l < r:

            amount = min(heights[l], heights[r])
            area = amount * (r - l)

            maximumWater = max(area, maximumWater)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maximumWater 
        