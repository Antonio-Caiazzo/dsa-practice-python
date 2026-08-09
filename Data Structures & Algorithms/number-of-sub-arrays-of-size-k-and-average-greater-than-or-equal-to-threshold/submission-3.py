class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg_to_pass = threshold * k
        track_avg = 0
        l = 0

        for i in range(k):
            track_avg += arr[i]
        
        result = 0 if track_avg < avg_to_pass else 1

        for r in range(k, len(arr)):
            track_avg -= arr[r - k]
            track_avg += arr[r]

            if track_avg >= avg_to_pass:
                result += 1

        return result

