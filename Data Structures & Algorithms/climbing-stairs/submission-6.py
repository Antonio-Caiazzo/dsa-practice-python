class Solution:
    def climbStairs(self, n: int) -> int:
        
        first_prev = 1
        second_prev = 1

        for _ in range(2, n + 1):
            new_value = first_prev + second_prev
            second_prev = first_prev
            first_prev = new_value
        
        return first_prev

