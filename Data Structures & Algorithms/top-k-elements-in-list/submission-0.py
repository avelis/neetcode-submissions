from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        arr = [[cnt, num] for num, cnt in counts.items()]

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res