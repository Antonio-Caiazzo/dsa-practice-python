class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window_sum = 0
        minimum_length = float("inf")

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                minimum_length = min(minimum_length, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return 0 if minimum_length == float("inf") else minimum_length