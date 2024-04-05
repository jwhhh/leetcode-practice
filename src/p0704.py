from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        range_min = 0
        range_max = len(nums)
        while range_min < range_max:
            range_mid = (range_min + range_max) // 2
            num_mid = nums[range_mid]
            if target == num_mid:
                return range_mid
            elif range_mid == range_min:
                break
            elif target < num_mid:
                range_max = range_mid
            elif target > num_mid:
                range_min = range_mid
        return -1
