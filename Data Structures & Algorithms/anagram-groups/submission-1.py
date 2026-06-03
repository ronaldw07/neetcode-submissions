class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        for string in strs:
            key = "".join(sorted(list(string)))
            
            if key not in seen:
                seen[key] = [string]
            else:
                seen[key].append(string)
        
        return list(seen.values())

        