class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(ship):
            total_weights = 0
            day = 1
            for weight in weights:
                total_weights += weight
                if total_weights > ship:
                    day += 1
                    total_weights = weight
            return day <= days

        lower, upper = max(weights), sum(weights)

        while lower < upper:

            mid = (lower + upper) // 2

            if check(mid):
                upper = mid
            else:
                lower = mid + 1
        return lower

        