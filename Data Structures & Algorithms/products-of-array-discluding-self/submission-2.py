class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        length = len(nums)




        #loop through, if i = 0 do all right 
        #else just multiply everything before it to everything after
        for i in range(len(nums)):
            if i == 0:
                res = 1
                for i in range(1,length):
                    res *= nums[i]

                output.append(res)   


            else:
                res = 1
                for j in range(i):
                    res *= nums[j] 
                
                for j in range(i + 1, len(nums)):
                    res *= nums[j]
                output.append(res)

        return output




