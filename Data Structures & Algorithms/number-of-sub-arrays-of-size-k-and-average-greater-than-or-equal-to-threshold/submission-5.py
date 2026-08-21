class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = 0

        for i in range(k):
            window += arr[i]
        
        result = 1 if window / k >= threshold else 0

        l = 0
        for r in range(k, len(arr)):
            window -= arr[l]
            window += arr[r]
            l += 1
            if window / k >= threshold:
                result += 1
        return result
        