class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        lists = list(s)
        listt = list(t)
        sorteds = sorted(s)
        sortedt = sorted(t)

        return sorteds == sortedt

