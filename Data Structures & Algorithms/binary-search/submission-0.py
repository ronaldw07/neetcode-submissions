class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary is choosing middle and checking if its less or more than middle
        #then serach in the new window
        l = 0


        r = len(nums) - 1


        while l <= r:

            m = r + l // 2 #would be 2 in [-1,0,2,4,6,8]

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

