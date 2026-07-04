from collections import Counter, deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = Counter(students)
        que = deque(students)
        for sandwiche in sandwiches:
            if count[sandwiche] == 0:
                break
            else:
                count[sandwiche] -= 1
                que.popleft()
        return len(que)

    
     

                

