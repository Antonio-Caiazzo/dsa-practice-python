class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0: 1}
        total = 0
        result = 0

        for num in nums:
            total += num
            remaining = total - goal

            result += prefix.get(remaining, 0)

            prefix[total] = prefix.get(total, 0) + 1

        return result
