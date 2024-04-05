from typing import List


# alternating subarray: no two adjacent elements in the subarray have the same value
class Solution:
    # [0, 1, 1, 1]
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        dp = [1]
        counter = 1
        for i in range(1, len(nums)):
            additional_count = 1 if nums[i] == nums[i-1] else dp[i-1] + 1
            dp.append(additional_count)
            counter += additional_count
        return counter
            
