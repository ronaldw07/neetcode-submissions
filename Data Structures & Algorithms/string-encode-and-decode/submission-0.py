class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result +=  str(len(s)) + "#" + s

        return result



    #[hi, hello, nihao]
    # s = 2#hi5#hello5#nihao




    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i #j start at 0
            while s[j] != "#": #while not equal to the limiter: add 1
                j += 1

            length = int(s[i:j])
            string = s[j+1: j + 1 + length]
            res.append(string)
            i = j + 1 + length

        return res
                 



