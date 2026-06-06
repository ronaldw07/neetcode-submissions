class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area is limited by the highest height 
        #so move the pointer of the lower one
        #keep track of area each time
        #compare to max and return it

        l = 0

        r = len(heights) - 1 #for length 8 start at 7

        maxarea = 0



        #test case = [1, 3,5,]
        while l < r:
            
            area = min(heights[l], heights[r]) * (r - l)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            maxarea = max(maxarea, area)

        return maxarea


        