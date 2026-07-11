import math

class AreaCalc:
    def calculate(self, *args):
        if len(args) == 1:
            result = math.pi * (args[0] * args[0])
            return round(result, 2)
        else:
            return args[0] * args[1]
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
