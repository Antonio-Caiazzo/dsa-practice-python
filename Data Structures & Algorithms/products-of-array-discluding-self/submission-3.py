class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix_product = 1
        suffix_product = 1
        for num in nums:
            result.append(prefix_product)
            prefix_product *= num

        for i in range(len(nums) - 1, -1, -1):
            result[i] = suffix_product * result [i]
            suffix_product *= nums[i]
        
        return result

        