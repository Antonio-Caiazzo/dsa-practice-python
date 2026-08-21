class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = 0
        check_value = k * threshold

        for i in range(k):
            window += arr[i]
        
        result = 1 if window >= check_value else 0

        l = 0
        for r in range(k, len(arr)):
            window -= arr[l]
            window += arr[r]
            l += 1
            if window >= check_value:
                result += 1
        return result
        