from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l_idx = 0
        r_idx = 1
        current_sum = nums[0]
        min_len_so_far = float("inf")
        while r_idx <= len(nums) and l_idx != r_idx:
            if current_sum >= target:
                current_diff = r_idx - l_idx
                min_len_so_far = min(min_len_so_far, current_diff)
                l_idx += 1
                current_sum -= nums[l_idx-1]
            else:
                r_idx += 1
                if r_idx <= len(nums):
                    current_sum += nums[r_idx-1]
        return min_len_so_far if min_len_so_far != float("inf") else 0
