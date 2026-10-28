class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total_sum = 0
        l = 0
        minimum_window = len(nums) + 1
        for r in range(len(nums)):
            total_sum += nums[r]

            while total_sum >= target:
                minimum_window = min(minimum_window, r - l + 1)
                total_sum -= nums[l]
                l += 1

        return 0 if minimum_window == len(nums) + 1 else minimum_window

        