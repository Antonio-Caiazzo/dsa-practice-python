class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        result = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                result += lmax- height[l]
                
                
            else:
                r -= 1
                rmax = max(rmax, height[r])
                result += rmax - height[r]
                
                
        return result

        
        [0,2,0,3,1,0,1,3,2,1]
        l = 1
        r = 9
        lmax = 0
        rmax= 1
        result = 0