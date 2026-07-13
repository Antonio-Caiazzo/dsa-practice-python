class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = l

        while l <= r:
            
            mid = l + (r - l) // 2

            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans
        