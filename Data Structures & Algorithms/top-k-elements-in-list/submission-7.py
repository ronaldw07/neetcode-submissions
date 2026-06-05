class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create buckets which each [i] represents the frequency and eachnumber 
        #in it is a number that has that frequency
        


        #test case [2,2,2,3,3,4]

        #creates [ [], [], [], [], [], [], [] ]
        count = [[] for i in range(len(nums) + 1)] # + 1 so it includes the max lnegth
        freq = {}


        #iterate through and store each key as the number and value as freq
        for num in nums:
            freq[num] = freq.get( num ,0) + 1

        


        #^ this creates {2:3, 3:2. 4:1, }

        #loop through the freq dictionary and store into buckets based on freq

        for key, value in freq.items():
            count[value].append(key)
        #creates [ [], [4], [3], [2], [], [], [] ]

        #reverse from the top of the buckets and add to a list (result), stopping at k
        result = []

        for i in range(len(count) -1 , 0, -1):

            for num in count[i]: #look through each num in the bucket (count[i])
                result.append(num)
                if len(result) == k:
                    return result


