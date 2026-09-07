class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        currPerm = []
        seen = set()
        def permutation():

            if len(currPerm) == len(nums):
                result.append(currPerm.copy())
                return

            for num in nums:
                if num in seen:
                    continue
                currPerm.append(num)
                seen.add(num)
                permutation()
                currPerm.pop()
                seen.remove(num)

        permutation()
        return result


        