class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,1,10]

        #buy low sell high
        #only check the profit if the right is bigger than the left
        #compare prof each time and set it to max if more 
        #return max at the end

        l = 0
        r = 1

        maxprofit = 0
        while r < len(prices):
            #if possible check profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit)
            else:
                l = r
            r += 1

        return maxprofit