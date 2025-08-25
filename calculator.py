# User input numbers
# operators + = / * log antilog conversion
# outputs answer
# add a gui


class calc:
    def __init__(self):
        return 0
    
    def add(self, x, y):
        self.x = x
        self.y = y
        return x + y
    
    def sub(self, x, y):
        self.x = x
        self.y = y
        return x - y
    
    def mul(self, x, y):
        self.x = x
        self.y = y
        return x * y
    
    def div(self, x, y):
        self.x = x
        self.y = y
        return x / y
    
    # How do we go about this
    def logic(self, operator):
        if operator == "add" or "+":
            return add(x, y)
        elif operator == "sub" or "-":
            return sub(x, y)
        elif operator == "mul" or "*":
            return mul(x, y)
        elif operator == "div" or "/":
            return div(x, y)
        else:
            return "Invalid operator"

    
x = float(input("Enter your first digit: "))
y = float(input("Enter your second digit: "))
operator = input("Enter your operator (add or +, sub or -, mul or *, div or /): ")
result = calc()
print(result)
