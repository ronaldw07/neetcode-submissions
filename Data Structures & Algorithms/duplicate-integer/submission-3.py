class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set to remove any extra duplicates
        #if length changes then return true
        #length of 3 vs 4
        return len(set(nums)) != len(nums)