class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum_area = float("-inf")

        while l < r:
            if heights[l] < heights[r]:
                maximum_area = max(maximum_area, heights[l] * (r - l))
                l += 1
            else:
                maximum_area = max(maximum_area, heights[r] * (r - l))
                r -= 1
        return maximum_area
            