class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_sequence = 0

        for num in nums:
            if num - 1 not in numbers:
                lenght = 1

                while num + 1 in numbers:
                    lenght += 1
                    num += 1
                
                max_sequence = max(max_sequence, lenght)
        return max_sequence

