class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, resultSet = [], []

        def helper(i):
            if i == len(nums):
                resultSet.append(currSet.copy())
                return

            currSet.append(nums[i])
            helper(i + 1)
            currSet.pop()

            helper(i + 1)

        helper(0)

        return resultSet