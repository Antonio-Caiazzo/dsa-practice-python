class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(capacity):
            day = 1
            start = 0
            for weight in weights:
                start += weight
                if start > capacity:
                    day += 1
                    start = weight
            return day <= days

        l, r = max(weights), sum(weights)

        while l < r:

            mid = (l + r) // 2

            if is_valid(mid):
                r = mid
            else:
                l = mid + 1
        
        return l