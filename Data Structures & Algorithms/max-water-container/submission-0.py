class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = float("-inf")

        while l < r:
            min_height = min(heights[l], heights[r])
            area = min_height * (r - l)
            if area > max_area:
                max_area = area
            else:
                if heights[l] > heights[r]:
                    r -=1
                else:
                    l += 1
        return max_area
            