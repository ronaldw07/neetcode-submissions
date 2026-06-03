class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, i in Counter(nums).most_common(k)]
        