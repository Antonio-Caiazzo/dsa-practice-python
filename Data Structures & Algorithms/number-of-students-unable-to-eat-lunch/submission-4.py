from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = Counter(students)
        
        for sandwiche in sandwiches:
            if count[sandwiche] == 0:
                break
            else:
                count[sandwiche] -= 1
                students.pop(0)
        return len(students)

    
     

                

