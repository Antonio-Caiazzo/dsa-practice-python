class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = {0: 1}
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            if current_sum - k in prefix:
                result += prefix[current_sum - k]

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return result
