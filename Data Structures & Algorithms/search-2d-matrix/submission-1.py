class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rrow = len(matrix) - 1
        rcolumn = len(matrix[0]) - 1
        lrow, lcolumn = 0, 0

        while lrow <= rrow:

            mr = (lrow + rrow) // 2

            if matrix[mr][0] == target:
                return True
            elif matrix[mr][0] <= target <= matrix[mr][rcolumn]:
                l = 0
                r = len(matrix[0]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mr][m] == target:
                        return True
                    elif matrix[mr][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                return False
            elif target > matrix[mr][rcolumn]:
                lrow = mr + 1
            else:
                rrow = mr - 1

        return False

        