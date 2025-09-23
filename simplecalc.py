class Calculator:
    def __init__(self, val1, val2):
        self.a = val1
        self.b = val2
    
    def add(self):
        # addition
        if type(self.a) == "str" and type(self.b) == "str":
            raise TypeError("Both arguments must be numbers")
        return self.a + self.b

    def subtract(self):
        # subtraction
        if type(self.a) == "str" and type(self.b) == "str":
            raise TypeError("Both arguments must be numbers")
        return self.a - self.b

    def multiply(self):
        # multiplication
        if type(self.a) == "str" and type(self.b) == "str":
            raise TypeError("Both arguments must be numbers")
        return self.a * self.b

    def divide(self):
        # division
        if type(self.a) == "str" and type(self.b) == "str":
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

    def power(self):
        # exponential
        if type(self.a) == "str" and type(self.b) == "str":
            raise TypeError("Both arguments must be numbers")
        return self.a ** self.b


nums = Calculator(5, 3)
# print(nums.subtract())
