class Solution:
 
    def encode(self, strs: List[str]) -> str:
        #"hello", "world" into hello world
        #build a big string with length then #
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
            
        return res

    def decode(self, s: str) -> List[str]:
        # 10#HelloWorld5#World
        #.       7
        result = []
        i = 0

        #take the number (len) then slice it starting past the # and add it to result

        while i < len(s):
            
            #j is used for slicing multi digit lengths of words
            j = i
            while s[j] != "#":
                j += 1
            
            wlength = int(s[i:j]) #10

            i = j + 1 #3
            j = i + wlength
            result.append(s[i:j]) #2 to 7

            i = j
        return result


        
        

