class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        result = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    total_sum = nums[i] + nums[j] + nums[k]
                    if total_sum == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(t) for t in result]
        '''
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1

        return result

