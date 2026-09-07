class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            new_tuple = self.two_sum(nums[i + 1:], -nums[i])
            for num in new_tuple:
                result.append([nums[i]] + num)

        return result

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        result = []
        l = 0
        r = len(nums) - 1

        while l < r:
            total_sum = nums[l] + nums[r]

            if total_sum == target:
                result.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1

                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif total_sum > target:
                r -= 1
            else:
                l += 1
        return result
