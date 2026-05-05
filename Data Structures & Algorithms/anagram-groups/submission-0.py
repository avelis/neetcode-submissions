from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for gram in strs:
            sorted_str = "".join(sorted(gram))
            groups[sorted_str].append(gram)
        return list(groups.values())
        