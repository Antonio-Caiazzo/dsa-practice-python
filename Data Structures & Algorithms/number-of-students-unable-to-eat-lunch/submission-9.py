class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circular = 0
        square = 0
        for student in students:
            if student:
                square += 1
            else:
                circular += 1

        for sandwiche in sandwiches:
            if sandwiche == 0 and circular <= 0:
                break
            elif sandwiche == 1 and square <= 0:
                break
            elif sandwiche == 0 and circular > 0:
                circular -= 1
            elif sandwiche == 1 and square > 0:
                square -= 1

        return square + circular