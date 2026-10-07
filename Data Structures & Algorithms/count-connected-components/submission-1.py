class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = {i: [] for i in range(n)}

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        num_connected = 0
        def dfs(v):
            if v in visited:
                return
            visited.add(v)

            for neighbor in adj_list[v]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for vertex in range(n):  
            if vertex not in visited:
                num_connected += 1
                dfs(vertex)

        dfs(0)
        return num_connected