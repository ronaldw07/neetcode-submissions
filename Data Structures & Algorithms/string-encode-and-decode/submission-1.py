class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        answer = []
        i = 0

        while i < len(s): #     4#hell5#hello
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j]) #4 and j = 1

            string = s[j+1 : j+1 + length]
            answer.append(string)
            i = j + 1 + length
                

        return answer
