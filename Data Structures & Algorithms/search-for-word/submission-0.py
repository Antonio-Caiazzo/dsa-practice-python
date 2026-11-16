class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = set()
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        def dfs(row, col, index):
            if index == len(word) - 1:
                return True

            visited.add((row, col))
        

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if not (0 <= nr < ROW and 0 <= nc < COL) or (nr, nc) in visited:
                    continue
                
                if board[nr][nc] == word[index + 1]:
                    if dfs(nr, nc, index + 1):
                        return True            
            visited.remove((row, col))

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False