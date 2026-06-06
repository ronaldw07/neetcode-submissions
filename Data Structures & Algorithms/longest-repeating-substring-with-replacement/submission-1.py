class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #loop through string
        #window - most common  has to be at most 1
        #test case 
        #so if "XXYZBY" = XXXZBY for k = 1
        #have left and right pointer
        #update length as window and compare max window sizes

        l = 0
        r = 0
        maxlen = 0

        count = {}
        #{X: 2, Y:1, Z:1}
        for r in range(len(s)): #loop through 0-5
            count[s[r]] = count.get(s[r], 0) + 1 # add on to the count in dict
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1


            maxlen = max(maxlen, r - l + 1)



        return maxlen


