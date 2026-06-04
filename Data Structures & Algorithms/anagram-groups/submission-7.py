class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop through list, (make each word a list then sort it to find the 
        #key then make the key

        # add onto the dictionary to make sure that each key is represented then output all values

        keys = {}

        for string in strs:

            sortedkey = sorted(list(string))
            key = "".join(sortedkey) #act = act and cat = act

            if key in keys:
                keys[key].append(string)
            else:
                keys[key] = [string]
            
        

        return list(keys.values())
