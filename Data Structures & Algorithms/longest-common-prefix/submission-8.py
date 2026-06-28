class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #sort the string so we only check through the range of the shortest (first one)

        

        #loop through the range of the shortest

        #if the character at the index is not the same as the others, the return up to the index

  

        for i in range(len(strs[0])):
            
            
            for word in strs:
                if len(word) == i or strs[0][i] != word[i]:
                    return strs[0][:i]
                
        return strs[0]

