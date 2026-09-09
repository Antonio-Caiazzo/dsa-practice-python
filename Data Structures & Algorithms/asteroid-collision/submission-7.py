class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            is_alive = True

            while len(stack) > 0 and stack[-1] > 0 and asteroid < 0:

                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    is_alive = False
                    break
                else:
                    is_alive = False
                    break
            
            if is_alive:
                stack.append(asteroid)

        return stack