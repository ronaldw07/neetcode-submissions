class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #array nums
        #sort array so its like [-4,-1,-1,0,1,2]

        res = []
        nums.sort()

        #enumerate loop through, if a is > 0 then break cuz no negatives

        
        for i, a in enumerate(nums):
            if a > 0:
                break

            #continue if the number is the same as before
            
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else: #adds to 0
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res