class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first make empty list of a bunch of lists
        #each index will represent the frequency of how many instances there are
        #eventually add onto a result and once the length hits (k) then return it


        bucket = [[] for i in range(len(nums) +1 )]
        count = {}

        for num in nums: # add to count first
            count[num] = count.get(num, 0) + 1 #{1:1 2: 2 3:3}
        
        for key, freq in count.items():
            bucket[freq].append(key) #[ [], [1], [2], [3]]

        result = []

        for i in range(len(nums), 0, -1): #start at len - 1 because reverse starts at the len but thats too high
            
            #starting at the highest freq bucket (len(nums) - 1 and working backwards)
            for num in bucket[i]: #for every number in bucket
                result.append(num) # add the number to result
                if len(result) == k: #once result length reaches k return it
                    return result
