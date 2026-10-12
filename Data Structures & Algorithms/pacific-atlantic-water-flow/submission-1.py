class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pacific = set()
        atlantic = set()
        def dfs(row, col, visited):
            visited.add((row, col))

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (0 <= nr < len(heights) and 0 <= nc < len(heights[0])) and (nr, nc) not in visited and heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, visited)
                    
                

        for row in range(len(heights)):
            dfs(row, 0, pacific)
        
        for col in range(len(heights[0])):
            dfs(0, col, pacific)

        for row in range(len(heights)):
            dfs(row, len(heights[0]) - 1, atlantic)
        
        for col in range(len(heights[0])):
            dfs(len(heights) - 1, col, atlantic)

        intersection = pacific & atlantic
        result = [[row, col] for row, col in intersection]
        return result

        