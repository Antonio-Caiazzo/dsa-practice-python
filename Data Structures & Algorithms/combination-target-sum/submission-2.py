class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        currComb = []
        nums.sort()

        def backtracking(total, start):
            if total == target:
                result.append(currComb.copy())
                return

            for j in range(start, len(nums)):
                if total + nums[j] > target:
                    break
                currComb.append(nums[j])
                backtracking(total + nums[j], j)
                currComb.pop()
                
        backtracking(0, 0)
        return result