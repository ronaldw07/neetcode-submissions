class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
           #make lists
        """
        make lists
        set them
        sort them
        compare
        
        """
        lists = list(s)
        listt = list(t)

        return sorted(lists) == sorted(listt)