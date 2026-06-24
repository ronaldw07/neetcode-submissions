class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #will the array be sorted


        #slidign window technique


        #prices = [10,2,5,6, 10,7,1,10]
                      


        l = 0
        r = 1

        maxP = 0

        while r < len(prices):

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)

            else:

                l = r
                
            r += 1

        return maxP



                