from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in frequency.items():
            bucket[freq].append(num)

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return []
