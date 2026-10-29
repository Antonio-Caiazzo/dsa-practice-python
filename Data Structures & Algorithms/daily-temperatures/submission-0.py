class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):

            while stack and stack[-1][1] < temperature:
                index, _ = stack.pop()
                answer[index] = (i - index)
            stack.append([i, temperature])
        
        return answer

                
