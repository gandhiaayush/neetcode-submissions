class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        s = 0
        l = len(heights) - 1
        while s < l:
            area = max((l - s) * min(heights[s], heights[l]), area)

            if heights[s] > heights[l]:
                l -= 1
            
            elif heights[l] > heights[s]:
                s += 1
            
            else:
                l -= 1
        
        return area
        