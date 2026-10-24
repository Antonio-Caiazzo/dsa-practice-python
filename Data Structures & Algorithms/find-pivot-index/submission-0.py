class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        total = prefix_sum[-1]

        for i in range(len(prefix_sum) - 1):
            if prefix_sum[i] == total - prefix_sum[i + 1]:
                return i

        return -1