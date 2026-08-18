class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float("inf")
        l = 0

        for r in range(len(nums)):
            target -= nums[r]
            while target <= 0:
                shortest = min(shortest, r - l + 1)
                target += nums[l]
                l += 1

        return shortest if shortest != float("inf") else 0
        