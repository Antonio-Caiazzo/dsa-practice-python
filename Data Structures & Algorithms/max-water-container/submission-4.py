class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        amount = 0

        while left < right:
            min_height = min(heights[left], heights[right])
            amount = max(amount, min_height * (right - left))

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1

        return amount


        