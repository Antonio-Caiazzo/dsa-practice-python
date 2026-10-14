class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {}

        for course, prereq in prerequisites:
            if course in adj_list:
                adj_list[course].append(prereq)
            else:
                adj_list[course] = [prereq]

        visiting, visited = set(), set()
        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True
            
            visiting.add(course)
            
            for c in adj_list.get(course, []):
                if not dfs(c):
                    return False
            visited.add(course)

            visiting.remove(course)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False

        return True