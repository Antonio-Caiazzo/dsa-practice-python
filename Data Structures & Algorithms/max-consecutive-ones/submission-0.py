class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        curr = 0
        for num in nums:
            if num:
                curr += 1
            else: 
                curr = 0
            if curr > maximum:
                maximum = curr

        return maximum 