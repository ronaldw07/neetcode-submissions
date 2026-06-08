class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #so innitially we can just go through the array and compare to target. it will take o(n) time and o(1)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1