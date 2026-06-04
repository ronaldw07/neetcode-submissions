class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)


        prefix = 1

        #nums = [1,2,4,6]
        #res = [1,1,1,1]
        #loop left to right
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        #the end should be
        #nums = [1,2,4,6]
        #rest [1, 1, 2, 8] - new

        
        #loop right to left
        postfix = 1
        for i in range(len(nums) -1, -1, -1): #work backwards
            res[i] *= postfix
            postfix *= nums[i]

        return res


        