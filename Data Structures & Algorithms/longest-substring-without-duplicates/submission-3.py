class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()

        l = 0
        maxlen = 0
        # ababcd
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            #if unique, add to set

            charSet.add(s[r])

            maxlen = max(maxlen, r - l + 1) # add + 1 cuz it starts at 0



            #{a,b, a} - { b,a,b} - {a,b,c} - {a,b,c,d}
        return maxlen