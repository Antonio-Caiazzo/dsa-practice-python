from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for s, d in prerequisites:
            courses[d].append(s)
            indegree[s] += 1

        queue = deque()
        visited = set()
        for i, node in enumerate(indegree):
            if node == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()

            for neighbor in courses[node]:
                if neighbor in visited:
                    continue
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    visited.add(neighbor)

        for node in indegree:
            if node != 0:
                return False
        return True
        