class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #enumerate for index and value
        #compare current number and see if it adds to target - > if it does return
        #if seen then add to a dictionary
        seen = {}
        
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i


        #seen = {3}

        #0, 3 need = 4
        #1, 4 need 3