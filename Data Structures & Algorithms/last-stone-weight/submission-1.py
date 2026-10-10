import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-x for x in stones]
        heapq.heapify(new_stones)

        while len(new_stones) >= 2:
            x = -heapq.heappop(new_stones)
            y = -heapq.heappop(new_stones)
            
            if x > y:
                heapq.heappush(new_stones, -(x-y))

        return -new_stones[0] if len(new_stones) == 1 else 0