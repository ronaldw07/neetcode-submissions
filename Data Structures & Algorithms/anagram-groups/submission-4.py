class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop through the array

        #group each string into a sorted word as a key with a hashmap

        # return the values as a list (no keys)

        anagrams = {}

        for word in strs:
            #change each word to list, then sort it to make the key and add
            #but the key must be immutable so make it a string 

            sortedlistword = sorted(list(word)) #hat turns into [a,h,t]
            key = "".join(sortedlistword) #key is aht

            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        return list(anagrams.values())



