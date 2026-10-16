class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        pacific = set()
        atlantic = set()
        ROW, COL = len(heights), len(heights[0])
        def dfs(row, col, visited):
            
            visited.add((row, col))

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if min(nr, nc) < 0 or nr >= ROW or nc >= COL or (nr, nc) in visited:
                    continue
                if heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, visited)


        for row in range(len(heights)):
            dfs(row, 0, pacific)
        for col in range(len(heights[0])):
            dfs(0, col, pacific)
        for row in range(len(heights)):
            dfs(row, len(heights[0]) - 1, atlantic)
        for col in range(len(heights[0])):
            dfs(len(heights) - 1, col, atlantic)

        return [[x, y] for x, y in pacific & atlantic]