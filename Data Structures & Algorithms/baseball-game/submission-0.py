class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == "C":
                stack.pop()

            elif op == "D":
                a = stack.pop()
                double = a * 2
                stack.append(a)
                stack.append(double)
            
            elif op == "+":
                a = stack.pop()
                b = stack.pop()
                result = a + b
                stack.append(b)
                stack.append(a)
                stack.append(result)
        
            else:
                stack.append(int(op))
            
                    
        return sum(stack)