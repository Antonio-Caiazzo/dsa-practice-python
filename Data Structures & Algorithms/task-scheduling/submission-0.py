from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequency = Counter(tasks)
        max_heap = [-count for count in frequency.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        t = 0

        while max_heap or cooldown:
            t += 1

            if cooldown and cooldown[0][1] <= t:
                count, _ = cooldown.popleft()
                heapq.heappush(max_heap, count)
            
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count < 0:
                    cooldown.append((count, t + n + 1))

        return t