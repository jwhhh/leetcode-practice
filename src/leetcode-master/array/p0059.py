from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        row_start = 0
        row_end = n
        col_start = 0
        col_end = n
        count = 1
        while count <= n**2:
            for i in range(col_start, col_end):
                matrix[row_start][i] = count
                count += 1
            if count > n**2:
                break
            row_start += 1
            for i in range(row_start, row_end):
                matrix[i][col_end-1] = count
                count += 1
            if count > n**2:
                break
            col_end -= 1
            for i in reversed(range(col_start, col_end)):
                matrix[row_end-1][i] = count
                count += 1
            if count > n**2:
                break
            row_end -= 1
            for i in reversed(range(row_start, row_end)):
                matrix[i][col_start] = count
                count += 1
            if count > n**2:
                break
            col_start += 1
        return matrix
            