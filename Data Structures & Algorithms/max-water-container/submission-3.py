class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        
        maxarea = 0
        while l < r:

            maxcurrentheight = min(heights[l], heights[r])

            currentarea =   maxcurrentheight * (r-l)
            maxarea = max(currentarea, maxarea)

            if heights[l] < heights[r]:
                l += 1
                      
            else:
                r -= 1 

        return maxarea