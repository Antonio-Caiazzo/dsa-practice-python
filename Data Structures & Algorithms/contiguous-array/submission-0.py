class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        maximum_length = 0
        prefix_sum = 0
        hashmap = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i

            else:
                maximum_length = max(maximum_length, i - hashmap[prefix_sum])

        return maximum_length
