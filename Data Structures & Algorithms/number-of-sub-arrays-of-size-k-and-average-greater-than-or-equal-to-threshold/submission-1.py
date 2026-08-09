class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        track_avg = 0
        l = 0

        for i in range(k):
            track_avg += arr[i]
        
        result = 0 if track_avg / k < threshold else 1

        for r in range(k, len(arr)):
            if r - l + 1 > k:
                track_avg -= arr[l]
                l += 1
            
            track_avg += arr[r]

            if track_avg / k >= threshold:
                result += 1

        return result

