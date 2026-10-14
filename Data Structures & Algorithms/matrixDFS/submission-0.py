class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        directions = [
            [1, 0],
            [-1 ,0],
            [0, 1],
            [0, -1]
        ]

        ROW, COL = len(grid), len(grid[0])
        
        def dfs(row, col, visited):
            
            if grid[row][col] == 1 or (row, col) in visited:
                return 0
            
            if row == ROW - 1 and col == COL - 1:
                return 1

            count = 0
            visited.add((row, col))

            for r, c in directions:
                nr = row + r
                nc = col + c
                if nc < 0 or nc == COL or nr < 0 or nr == ROW:
                    continue
                count += dfs(nr, nc, visited)

            visited.remove((row, col))
            return count
            

        return dfs(0, 0, set())