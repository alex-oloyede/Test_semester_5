class Calculator:
    
    def add(self, a, b):
        # addition
        if type(a) == "str" and type(b) == "str":
            raise TypeError("Both arguments must be numbers")
        return a + b
    
    def subtract(self, a, b):
        # subtraction
        if type(a) == "str" and type(b) == "str":
            raise TypeError("Both arguments must be numbers")
        return a - b
    
    def multiply(self, a, b):
        # multiplication
        if type(a) == "str" and type(b) == "str":
            raise TypeError("Both arguments must be numbers")
        return a * b
    
    def divide(self, a, b):
        # division
        if type(a) == "str" and type(b) == "str":
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        # exponential
        if type(a) == "str" and type(b) == "str":
            raise TypeError("Both arguments must be numbers")
        return base ** exponent
