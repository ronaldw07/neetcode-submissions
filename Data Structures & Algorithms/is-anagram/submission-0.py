class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        lists = list(s) #[r, a, c, e, c, a, r]
        listt = list(t)

        sortedt = sorted(t)
        sorteds = sorted(s)

        #now you compare the sorted and return true if they are equal

        if sortedt == sorteds:
            return True
        else:
            return False
        