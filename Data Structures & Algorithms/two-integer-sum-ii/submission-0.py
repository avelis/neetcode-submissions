class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1

        while right_idx > 0:
            if numbers[left_idx] + numbers[right_idx] > target:
                right_idx -= 1
            if numbers[left_idx] + numbers[right_idx] < target:
                left_idx += 1
            if numbers[left_idx] + numbers[right_idx] == target:
                return [left_idx + 1, right_idx + 1]
        return []