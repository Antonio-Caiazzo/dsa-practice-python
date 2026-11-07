class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        l = 0
        min_sub_sequence = float("inf")
        for r in range (len(nums)):
            window += nums[r]

            while window >= target:
                min_sub_sequence = min(min_sub_sequence, r - l + 1)
                window -= nums[l]
                l += 1
                
        return min_sub_sequence if min_sub_sequence != float("inf") else 0
        