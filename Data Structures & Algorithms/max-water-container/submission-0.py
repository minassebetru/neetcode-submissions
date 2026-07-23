class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        maxarea = 0

        while l < r:
            lower = min(heights[l], heights[r])
            distance = (r - l)
            area = lower * distance
            maxarea = max(area, maxarea)

            if heights[l] < heights [r]:
                l += 1
                print(l, r)
            else:
                r -= 1
        
        return maxarea