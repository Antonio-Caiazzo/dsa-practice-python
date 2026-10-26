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
'''
[1,1,1,1,1]
total = 5
result = 1
remaining = 1
prefix{0: 2, -2: 1, -1: 1, 1: 1}
'''