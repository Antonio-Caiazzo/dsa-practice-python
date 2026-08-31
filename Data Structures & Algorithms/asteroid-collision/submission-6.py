class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            is_alive = True
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    is_alive = False
                    break

                else:
                    is_alive = False
                    break

            if is_alive:
                stack.append(asteroid)

        return stack
            
