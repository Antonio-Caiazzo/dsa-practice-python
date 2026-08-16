class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read = 1

        for write in range(1, len(nums)):

            if nums[write] != nums[read - 1]:
                nums[read] = nums[write]
                read += 1
        
        return read
        