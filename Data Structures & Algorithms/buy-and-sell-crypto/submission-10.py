class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        



        #will prices length be at least 1?
        #will it be sorted?    
        #left should be less than right

        #while l is left than r

        #keep a max profit counter and return at the end
        
        #[10,1,5,6,7,1,10]
        maxP = 0
        l = 0
        r = 1

        while l < r and r < len(prices):

            
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit) #4, 5, 6 
            if prices[l] >= prices[r]:
                l = r
            r += 1

        return maxP