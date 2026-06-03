class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for string in strs: #loop through list
            key = "".join(sorted(list(string)))

            if key not in anagrams:
                anagrams[key] = [string]
            else:
                anagrams[key].append(string)
            
        return list(anagrams.values())

        