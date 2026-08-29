class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = height[0]
        rmax = height[-1]
        l, r = 0, len(height) - 1
        amount = 0
        while l <= r:
            if lmax <= rmax:
                lmax = max(lmax, height[l])
                amount += (lmax - height[l])
                l += 1
            else:
                rmax = max(rmax, height[r])
                amount += (rmax - height[r])
                r -= 1
        return amount

        