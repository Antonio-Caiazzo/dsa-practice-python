class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)

        max_len = 0
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + 1 in seen:
                    num += 1
                    length += 1
                max_len = max(max_len, length)

        return max_len



