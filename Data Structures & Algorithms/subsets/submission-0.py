from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[], nums]

        subsets = [[],]
        for i in range(len(nums)):
            subsets.extend(combinations(nums, i+1))
        
        return [list(s) for s in subsets]