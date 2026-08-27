class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            total_sum = -nums[i]
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                value = nums[l] + nums[r]
                if value == total_sum:
                    result.append([-total_sum, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif value > total_sum:
                    r -= 1
                else:
                    l += 1
        return result
