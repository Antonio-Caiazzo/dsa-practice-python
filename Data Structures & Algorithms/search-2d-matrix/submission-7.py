class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        ROW = len(matrix)
        COL = len(matrix[0])

        left_row, right_row = 0, ROW - 1

        while left_row <= right_row:

            mid_row = (left_row + right_row) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][COL - 1]:
                left, right = 0, COL - 1
                while left <= right:
                    mid = (left + right) // 2

                    if matrix[mid_row][mid] < target:
                        left = mid + 1
                    elif matrix[mid_row][mid] > target:
                        right = mid - 1
                    else:
                        return True
                return False
            elif matrix[mid_row][0] > target:
                right_row = mid_row - 1
            else:
                left_row = mid_row + 1
        return False