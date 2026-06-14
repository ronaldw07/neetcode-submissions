class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #test case
        #nums = [1,2,2,2,3,3,3] k = 2 


        #asking:
        #is nums already sorted in ascending order
        #what is the minimum k
        #and what is the minimum length for array nums

        #k will be a counter in the end


        #need way to seperate the count of each
        #then return the (k)numbers within the highest counts

        #creating a list of lists where each list index represents the frequency of each number 
        #within the original numms array

        freq = [[] for i in range(len(nums) + 1)]
        #[0 , 1, 2, 3, 4, 5, 6, 7]


        #dictionary to track each number's count


        #return the dictionary sorted in the end
        count = {}

        #{1 : 1, 2: 2, 3:3}

        for num in nums:
            count[num] = count.get(num, 0) + 1 #update the value for respective key
            
        for key, num in count.items():
            freq[num].append(key)


        result  = []
        count = 0

        #go backwards in the freq list to grab the most frequent ones and add to result
        for i in range(len(freq) - 1, -1, -1): #end -1 so 0 is included
            for num in freq[i]:
                result.append(num)
                count += 1
                if count == k:
                    return result
                    
            
                

                
                


                
                
                

                





