from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prerequisite = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for s, d in prerequisites:
            prerequisite[d].append(s)
            indegree[s] += 1

        queue = deque()
        result = []

        for i, node in enumerate(indegree):
            if node == 0:
                queue.append(i)
                result.append(i)
        
        while queue:

            node = queue.popleft()

            for neighbor in prerequisite[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(neighbor)
        
        return result if len(result) == numCourses else []


        