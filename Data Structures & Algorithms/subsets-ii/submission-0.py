from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)+1):
            for combo in combinations(nums, i):
                if combo not in output:
                    output.append(combo)
        return output

