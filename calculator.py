# User input numbers
# operators + = / * log antilog conversion
# outputs answer
# add a gui


class Calc:
    def __init__(self):
        pass  # No need to return anything

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

    def logic(self, x, y, operator):
        if operator in ["add", "+"]:
            return self.add(x, y)
        elif operator in ["sub", "-"]:
            return self.sub(x, y)
        elif operator in ["mul", "*"]:
            return self.mul(x, y)
        elif operator in ["div", "/"]:
            return self.div(x, y)
        else:
            return "Invalid operator"

    
# 🧪 Execution
x = float(input("Enter your first digit: "))
y = float(input("Enter your second digit: "))
operator = input("Enter your operator (add or +, sub or -, mul or *, div or /): ")

calc = Calc()
result = calc.logic(x, y, operator)
print("Result:", result)
