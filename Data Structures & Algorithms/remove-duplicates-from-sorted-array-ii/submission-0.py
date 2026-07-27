class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        count = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                count = 1
                nums[write] = nums[read]
                write += 1
            else:
                if count < 2:
                    nums[write] = nums[read]
                    count += 1
                    write += 1

        return write
                
        