class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                l = i + 1
                r = n - 1
                while l < r:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if curr_sum > 0:
                        r -= 1
                    elif curr_sum < 0:
                        l += 1
                    else:
                        result.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                        while l < r and nums[r + 1] == nums[r]:
                            r -= 1
        return result

        