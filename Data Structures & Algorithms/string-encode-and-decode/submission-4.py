class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res


        #combine all strings to a string wiht length then #
    def decode(self, s: str) -> List[str]:
        

        # 10#HelloWorld5#World
        #---------------------
        i = 0
        result = []
        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1
            #j = 2 initially
            length = int(s[i:j]) #10
            i = j + 1 #start at the word right after the #
            j = i + length #slice word out

            result.append(s[i:j])

            i = j
        return result




