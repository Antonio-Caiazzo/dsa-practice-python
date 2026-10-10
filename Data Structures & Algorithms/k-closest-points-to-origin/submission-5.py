import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for x, y in points:
             
            distance = (x**2) + (y**2)
            heapq.heappush(result, (-distance, x, y))   
            if len(result) > k:
                heapq.heappop(result)
                
        return [[x, y] for _, x, y in result]

