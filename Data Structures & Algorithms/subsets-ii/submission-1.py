class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        nums.sort()

        def subset(i):
            if i == len(nums):
                result.append(curr.copy())
                return
            
            
            curr.append(nums[i])
            subset(i + 1)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            subset(i + 1)

        subset(0)
        return result

        