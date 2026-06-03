class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first make both string into lists so we can use sort them and compare

        #sort changes in place vs sorted() which is copy which takes moore memory
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        