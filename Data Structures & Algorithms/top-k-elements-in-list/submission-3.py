class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force first. key is the number

        #make set to track it 
        #then sort it
        #then return the result of the k most frequent

        keys = {}

        for num in nums:
            if num in keys:
                keys[num] += 1
            else:
                keys[num] = 1

        #{1:1, 2:2, 3:3}

        highestval = sorted(list(keys.values()), reverse=True) #[3, 2, 1]

        result = []

        for i in range(k): #0, 1
            val = highestval[i]
            for key, count in keys.items():
                if val == count and key not in result:
                    result.append(key)

        return result


