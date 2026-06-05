class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 #buy low sell high
        r = 1
        maxprof = 0

        # test case[5,1,5,6,7,1,10]
        #max = 6

        while r < (len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprof = max(profit, maxprof)
            else:
                l = r
                
            r += 1

        return maxprof


