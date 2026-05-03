class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1

        while left_idx < right_idx:
            tmp_sum = numbers[left_idx] + numbers[right_idx]
            if tmp_sum > target:
                right_idx -= 1
            elif tmp_sum < target:
                left_idx += 1
            else:
                return [left_idx + 1, right_idx + 1]
        return []