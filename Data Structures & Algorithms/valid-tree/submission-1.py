class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = {i: [] for i in range(n)}

        for s, d in edges:
            adj_list[s].append(d)
            adj_list[d].append(s)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for vertex in adj_list[node]:
                if vertex not in visited:
                    dfs(vertex)
        
        dfs(0)        
        return len(visited) == n