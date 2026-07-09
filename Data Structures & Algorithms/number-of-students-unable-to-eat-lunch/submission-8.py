from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:


        square_student = students.count(1)
        circular_student = students.count(0)

        for sandwiche in sandwiches:
            if sandwiche == 1 and square_student == 0:
                break

            elif sandwiche == 0 and circular_student == 0:
                break

            elif sandwiche == 1 and square_student > 0:
                square_student -= 1

            elif sandwiche == 0 and circular_student > 0:
                circular_student -= 1

            



        return max(circular_student, square_student)

        