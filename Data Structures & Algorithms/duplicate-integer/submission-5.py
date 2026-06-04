class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #compare lengths after set

        seen = []

        for num in nums:
            if num in seen:
                return True

            seen.append(num)

        return False