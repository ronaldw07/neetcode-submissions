class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set up two pointers
        #move right accordingly and compare to the max
        #if the right is smaller than the right, move the left to where the righ tis
        #return at the end

        l = 0
        maxP = 0
        r = 1


        #test case 3 = [1,5,6,7,1,10]
        while r < len(prices):
            #if r is more than the left: then compute profit and store
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: #if it is not, shift left up and also have right
                l = r
            #increment to keep moving on:
            r += 1


        

        return maxP
        