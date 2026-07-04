class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            count = 0

            for pile in piles:
                count += (pile + k - 1) // k
                if count > h:
                    return 0
            return 1

        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2

            if check(m):
                r = m - 1
            else:
                l = m + 1
        
        return l


    


