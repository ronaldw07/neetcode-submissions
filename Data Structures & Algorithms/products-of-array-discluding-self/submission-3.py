class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        #nums = [1,2,4,6]
        #res = [1,1,1,1]
        
        

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]       

        #end of left to right should be res =  [1,1,2,8]



        #nums = [1,2,4,6]
        #res =  [1,1,2,8]

        #right to left
        postfix = 1
        for i in range(len(nums)- 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]   

        return res
        #ending should be 

             