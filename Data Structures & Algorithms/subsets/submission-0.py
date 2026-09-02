class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, resultSet = [], []

        def helper(i, nums):
            if i == len(nums):
                resultSet.append(currSet.copy())
                return

            currSet.append(nums[i])
            helper(i + 1, nums)
            currSet.pop()

            helper(i + 1, nums)

        helper(0, nums)

        return resultSet