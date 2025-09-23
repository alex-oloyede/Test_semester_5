class Calculator:
    def __init__(self, val1, val2):
        self.a = val1
        self.b = val2
    
    def add(self):
        # addition
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return self.a + self.b

    def subtract(self):
        # subtraction
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return self.a - self.b

    def multiply(self):
        # multiplication
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return self.a * self.b

    def divide(self):
        # division
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

    def power(self):
        # exponential
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return self.a ** self.b


nums = Calculator(5, 3)
# print(nums.subtract())
