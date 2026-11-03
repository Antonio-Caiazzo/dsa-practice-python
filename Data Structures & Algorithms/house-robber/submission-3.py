class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)


        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        maximumMoney = 0

        for i in range(2, len(nums)):
            
            new_value = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = new_value            

        return prev1

        