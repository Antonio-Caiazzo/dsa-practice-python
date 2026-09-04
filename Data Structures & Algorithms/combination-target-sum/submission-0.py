class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        currComb = []

        def backtracking(value, i):
            if value == target:
                result.append(currComb.copy())
                return

            for j in range(i, len(nums)):
                if value + nums[j] > target:
                    continue
                currComb.append(nums[j])
                backtracking(value + nums[j], j)
                currComb.pop()
                
        backtracking(0, 0)
        return result