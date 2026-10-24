class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)

        for i, num in enumerate(nums):
            rightSum = total - num - leftSum
            if leftSum == rightSum:
                return i
            leftSum += num
        return -1