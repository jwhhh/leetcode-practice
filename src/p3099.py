class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        tmp_x = x
        sum_digits = 0
        while True:
            sum_digits += tmp_x % 10
            tmp_x = tmp_x // 10
            if tmp_x < 1:
                break
        return sum_digits if x % sum_digits == 0 else -1
