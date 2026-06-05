class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,6, 1 ,7] - max would be 6
        l = 0
        r = 1 #buy low sell high

        maxP = 0

        while r < len(prices): # loop through the array
            if prices[l] < prices[r]:

                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r

            r += 1
        return maxP
        

