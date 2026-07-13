class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            if self.feasible(mid, piles, h):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, k, piles, h):
        count = 0
        for pile in piles:
            count += (pile + k - 1) // k
        return True if count <= h else False

    



        