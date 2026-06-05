class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a big frequency map (list of lists that each bucket holds how manytimes each number appears)
        #eery index of each bucket represents how many times its there [i] = freq so i=1 = freq i
        #then return a list starting at the highest range and work backwards and stop once i = 2

        count = {}

        freq = [[] for i in range(len(nums)+1)] #[[], [], [], [], [], [],[]]

        count = {}
        # [0, 1, 2, 3]
        
        for num in nums:
            count[num] = count.get(num, 0) + 1 #{1:1 2:2, 3:3}
        
        for key, values in count.items(): #[[],[1],[2],[3]]
            freq[values].append(key)

        result = []
        
        for i in range(len(nums), 0, -1): #start at len 
            
            #starting at the highest freq bucket (len(nums)  and working backwards)
            for num in freq[i]: #for every number in bucket
                result.append(num) # add the number to result
                if len(result) == k: #once result length reaches k return it
                    return result
        

