class Solution:
    def robLinear(self, nums: List[int], start: int, end: int) -> int:
        
        if start == end:
            return nums[start]
        
        prev2 = nums[start]
        prev1 = max(prev2, nums[start + 1])

        for i in range(start + 2, end + 1):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        return prev1

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        return max(self.robLinear(nums, 0, len(nums) - 2), self.robLinear(nums, 1, len(nums) - 1))