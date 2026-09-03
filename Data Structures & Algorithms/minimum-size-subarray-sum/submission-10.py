class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        window = len(nums) + 1
        window_sum = 0
        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                window = min(window, r - l + 1)
                window_sum -= nums[l]
                l += 1
                
        return 0 if window == len(nums) + 1 else window
