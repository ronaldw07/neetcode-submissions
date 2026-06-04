class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        #enumerate through
        #eliminate if a value starts more than 0 because its not possible to equal 0 then
        #continue if value is same left neighbor

        #set = [-4,-1,-1,0,1,2]

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #now use two pointers and iterate through

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 # add one so move on to next set
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res










