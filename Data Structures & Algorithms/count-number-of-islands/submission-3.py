class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col):

            if not (0 <= row < ROWS) or not (0 <= col < COLS) or grid[row][col] == "0" or (row, col) in visited:
                return

            visited.add((row, col))

            for dr, dc in directions:
                newRow = dr + row
                newCol = dc + col

                dfs(newRow, newCol)

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == "1":
                    island += 1
                    dfs(row, col)

        return island
