class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x // 2
        if x < 2:
            return x
        result = -1
        while l <= r:
            m = (l+r) // 2
            if m*m == x:
                return m
            elif m * m < x:
                result = m
                l = m + 1
            else:
                r = m - 1
        return result

        