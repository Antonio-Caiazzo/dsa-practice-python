class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            is_alive = True

            if asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop() 
                if stack and stack[-1] == -asteroid:
                    is_alive = False
                    stack.pop()  
                elif stack and stack[-1] > abs(asteroid):
                    is_alive = False             
            
            if is_alive:
                stack.append(asteroid)

        return stack
        

