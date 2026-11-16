from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        fresh = 0
        minute = 0
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        while queue:
            level_size = len(queue)
            areChange = fresh

            for _ in range(level_size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if not (0 <= nr < ROW and 0 <= nc < COL) or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

            if fresh != areChange:
                minute += 1
        
        return minute if fresh == 0 else -1
            
        









        