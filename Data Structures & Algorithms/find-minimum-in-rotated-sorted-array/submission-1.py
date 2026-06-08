class Solution:
    def findMin(self, nums: List[int]) -> int:
        #two pointers l and r
        # compare current to the right
        #if the right is smaller, the move window to the middle and up
        # keep repeating then return when l = r



        l = 0
        r = len(nums) - 1



        while l < r:
            m = (l + r) // 2 
            if nums[m] < nums[r]:
                r = m

            else:
                l = m + 1
        return nums[l]