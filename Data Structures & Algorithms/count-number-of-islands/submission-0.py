class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        len_rows = len(grid)
        len_cols = len(grid[0])
        num_islands = 0
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        
        def dfs(row, col):
            visited.add((row, col))

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (new_row < 0 or new_row >= len_rows or new_col < 0 or new_col >= len_cols):
                    continue
                
                if grid[new_row][new_col] != "1":
                    continue
                
                if (new_row, new_col) in visited:
                    continue
                
                
                dfs(new_row, new_col)
                
        for row in range(len_rows):
            for col in range(len_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_islands += 1
                    dfs(row, col)                    
        
        return num_islands

