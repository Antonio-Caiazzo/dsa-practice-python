from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        change = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        while 0 < len(sandwiches) and change < len(sandwiches):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                change = 0
            else:
                students.append(students.popleft())
                change += 1
        return len(sandwiches)