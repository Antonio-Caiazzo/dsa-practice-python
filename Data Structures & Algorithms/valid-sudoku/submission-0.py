class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]        
        quadrants = {}
        for i in range(3):
            for j in range(3):
                quadrants[(i, j)] = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                box_key = (r // 3, c // 3)
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in quadrants[box_key]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                quadrants[box_key].append(board[r][c])

        return True