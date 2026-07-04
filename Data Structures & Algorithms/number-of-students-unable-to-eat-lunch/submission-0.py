from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rifiuti = 0
        coda = deque(students)
        while rifiuti != len(coda):
            if coda[0] == sandwiches[0]:
                coda.popleft()
                sandwiches.pop(0)
                rifiuti = 0
            else:
                coda.append(coda.popleft())
                rifiuti += 1
        return len(coda)