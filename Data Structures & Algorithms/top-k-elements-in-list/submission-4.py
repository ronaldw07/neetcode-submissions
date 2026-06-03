class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedlist = Counter(nums)
        #returns Counter({1:1, 2:2, 3:3})

        result = countedlist.most_common(k)

        #returns [(3,3), (2,2)]

        return [count for count, num in result]