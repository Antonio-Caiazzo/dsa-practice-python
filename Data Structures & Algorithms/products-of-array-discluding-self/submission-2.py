class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        prefix = []
        for num in nums:
            prefix.append(product)
            product *= num
    
        product = 1
        suffix = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result

        