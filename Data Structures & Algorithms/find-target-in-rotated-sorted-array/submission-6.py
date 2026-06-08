class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #so obviously set up left and right pointers


        #test cases: target = 1
        #[2,3,4,5,6,1] one where target it on the right side

        #[4,5,6,1,2,3]
        #[3,4,5,6,1,2]
        
        #[6,1,2,3,4,5] one where target is on left
        #must compare both sides


        #check in a while loop l < r
        #check middle first
        #if current is the target, then return the cur. index. - always check

        #if not, check to see if it would be in the left or right
        #check if the left or right is sorted
        
         #move window accordingly and return when window gets to the target
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: #left side sorted
                if nums[l] > target or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] < target or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
        
        #test case = [4,5,6,7,0,1,2] target = 4
                    #[4,5,6]
                    #[4]
                    #[0,1,2,3,4,5,6]   m = 3. | result = 4


                    

    






