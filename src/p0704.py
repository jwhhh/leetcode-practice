from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        range_min = 0
        range_max = len(nums) - 1
        while range_min <= range_max:
            range_mid = (range_min + range_max) // 2
            num_mid = nums[range_mid]
            if num_mid < target:
                range_min = range_mid + 1
            elif num_mid > target:
                range_max = range_mid - 1
            else:
                return range_mid
        return -1
