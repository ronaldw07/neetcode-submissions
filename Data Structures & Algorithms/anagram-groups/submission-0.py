class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        values = defaultdict(list)
        for string in strs: #loop through each string in str
             
            key = "".join(sorted(string)) #act: act and cat |outputs ['a', 'c', 't']
            values[key].append(string) #default dict creates empty list if no key
            
        return list(values.values()) #answer