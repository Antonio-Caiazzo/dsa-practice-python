class Solution:
    def binarySearch(self, nums, target, findFirst):

        left, right = 0, len(nums) - 1
        index = -1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if findFirst:
                    index = mid
                    right = mid - 1
                else:
                    index = mid
                    left = mid + 1 

        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.binarySearch(nums, target, True),
            self.binarySearch(nums, target, False)
        ]