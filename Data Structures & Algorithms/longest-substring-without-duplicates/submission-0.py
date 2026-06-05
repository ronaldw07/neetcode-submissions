class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        charset = set()
        longest = 0

        #increase window until duplicate character found

        # abcabcd
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1




            charset.add(s[r])
            longest = max(longest, r - l + 1)

            

        #charset = {a,b,c} - {b,c,a} - {}
        return longest




            
            

            