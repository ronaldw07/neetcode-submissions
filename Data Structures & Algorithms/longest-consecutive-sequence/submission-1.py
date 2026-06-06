class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        numset = set(nums)
        longest = 0
        #if no neighbor on the left, then start of length


        #[2,3,1,4,6]
        for num in numset:
            if num - 1 not in numset: #if not there then start of sequence
                length = 1
                while (num + length) in numset: #( check to see if next number is there) while 2 is in it
                    length += 1

                longest = max(length, longest)
        return longest


        