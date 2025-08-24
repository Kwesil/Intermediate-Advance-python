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
    
    def logic(self, operator):
        if operator == "addition":
            return add(x, y)

        return{}

    
x = float(input("Enter your first digit: "))
y = float(input("Enter your second digit: "))
operator = input("Enter your operator (addition subtraction, muliplication, division): ")
