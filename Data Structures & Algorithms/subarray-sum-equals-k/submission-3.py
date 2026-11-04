class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        result = 0
        currentSum = 0

        for num in nums:
            currentSum += num

            if currentSum - k in prefix:
                result += prefix[currentSum - k]

            prefix[currentSum] = prefix.get(currentSum, 0) + 1

        return result

