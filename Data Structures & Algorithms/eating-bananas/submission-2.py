import math
class Solution:

    def canEat(self, bananaHour, h, piles):

        totalHours = 0

        for pile in piles:

            totalHours += math.ceil(pile/bananaHour)

        return totalHours <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        while l < r:

            mid = (l + r) // 2

            if self.canEat(mid, h, piles):
                r = mid
            else:
                l = mid + 1

        return l
        
