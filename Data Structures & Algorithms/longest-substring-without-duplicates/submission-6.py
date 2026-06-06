class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #start left and right two pointers
        #if character is already in the set; compare and set max accordingly



        # "pwwkew" should return 3

        l = 0
        seen = set()
        maxlen = 0 #3
        
        #seen = {,k,e,w}
        for r in range(len(s)): #check if each character is in the set ; if not yet then update length
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxlen = max(maxlen, r-l+1)
            
            
        return maxlen

