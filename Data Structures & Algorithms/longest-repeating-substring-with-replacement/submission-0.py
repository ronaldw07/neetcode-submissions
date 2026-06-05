class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #s for string
        #k for length


        # AAABCBB

        #start with l and right together on left and right
        l = 0
        
        count = {}
        maxfreq = 0

        # add every letter and the count wihtin the range
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 #{A:1}
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1 #{A:3} to {A:2}
                l += 1

            
            
            maxfreq = max(maxfreq, (r - l + 1)) #compare between past and size of window
            
        return maxfreq

        #{A:3, B:1, C:1}
        #right = 0, 1, 2, 3, 4
        #maxfrq= 1, 2, 3, 4,

