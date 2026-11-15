import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            current_dist, node = heapq.heappop(min_heap)

            if current_dist > dist[node]:
                continue

            for neighbor, weight in graph.get(node, []):
                cost = weight + current_dist

                if dist[neighbor] > cost:
                    dist[neighbor] = cost
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
        maximum = float("-inf")
        for i in range(1, len(dist)):
            if dist[i] == float("inf"):
                return -1
            maximum = max(maximum, dist[i])
        
        return maximum
            
