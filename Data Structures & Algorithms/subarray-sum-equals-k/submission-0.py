class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        result = running_sum = 0

        for num in nums:
            running_sum += num

            result += prefix.get(running_sum - k, 0)
            prefix[running_sum] = prefix.get(running_sum, 0) + 1

        return result