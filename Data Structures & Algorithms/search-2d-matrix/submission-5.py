class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rrow = len(matrix) - 1 
        rcolumn = len(matrix[0]) - 1
        lrow = 0
        while lrow <= rrow:
            mrow = (lrow + rrow) // 2
            if matrix[mrow][0] == target:
                return True

            elif matrix[mrow][0] < target <= matrix[mrow][rcolumn]:
                left = 0
                right = rcolumn

                while left <= right:
                    mcolumn = (left + right) // 2

                    if matrix[mrow][mcolumn] == target:
                        return True
                    elif matrix[mrow][mcolumn] < target:
                        left = mcolumn + 1
                    else:
                        right = mcolumn - 1
                return False

            elif matrix[mrow][0] < target:
                lrow = mrow + 1

            else:
                rrow = mrow - 1
        return False

