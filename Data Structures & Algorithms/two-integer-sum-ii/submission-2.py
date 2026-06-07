class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two sum  but index1 < index2

        #[1,2,3,5,6,8]

        #target = 3

        #1 indexed instead of 0
        #so just output the two that add up to target and just add 1 to the result
        #use hashmap to track seen
        #make target eery time and once satisfied return

        
         
        seen = {}
        
        #store value and the index it is at
        #seen = {1,}


        for i in range(len(numbers)):
            
            needed = target - numbers[i]
            if needed in seen:
                return [seen[needed], i+1]

            seen[numbers[i]] = i + 1

        


