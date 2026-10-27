class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)
        maximumLongest = 1
        currMax = 1

        for num in nums:
            if num - 1 not in numbers:
                while num + 1 in numbers:
                    num += 1
                    currMax += 1
                    maximumLongest = max(currMax, maximumLongest)

                currMax = 1
        return maximumLongest