class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        currPerm = []
        def permutation():

            if len(currPerm) == len(nums):
                result.append(currPerm.copy())
                return

            for num in nums:
                if num in currPerm:
                    continue
                currPerm.append(num)
                permutation()
                currPerm.pop()

        permutation()
        return result


        