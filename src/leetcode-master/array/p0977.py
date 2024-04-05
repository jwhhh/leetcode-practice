from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        idx_left = 0
        idx_right = len(nums) - 1
        square_left = nums[idx_left] ** 2
        square_right = nums[idx_right] ** 2
        idx = len(nums) - 1
        while idx >= 0:
            if square_left >= square_right:
                result[idx] = square_left
                idx_left += 1
                if idx_left < len(nums):
                    square_left = nums[idx_left] ** 2
            else:
                result[idx] = square_right
                idx_right -= 1
                if idx_right >= 0:
                    square_right = nums[idx_right] ** 2
            idx -= 1
        return result
        
        