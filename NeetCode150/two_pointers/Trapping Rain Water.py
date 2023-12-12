class Solution:
    def trap(self, height: List[int]) -> int: 
        if len(height) <= 2:
            return 0
        
        ans = 0
        l = 0
        r = len(height) - 1
        lMax = height[0]
        rMax = height[-1]

        while l < r:
            if lMax < height[l]:
                lMax = height[l]
            if rMax < height[r]:
                rMax = height[r]
            
            if lMax <= rMax:
                ans += lMax - height[l]
                l += 1
            else:
                ans += rMax - height[r]
                r -= 1
        
        return ans