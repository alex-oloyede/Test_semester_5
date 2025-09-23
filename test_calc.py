import pytest
from test import Calculator

# Test 1: Addition tests
def test_add_positive():
    # Arrange
    a, b = 5, 3
    expected = 8

    # Act
    result = Calculator(5, 3).add()

    # Assert
    assert result == expected

def test_add_negative_numbers():
    # Arrange
    a, b = -5, -3
    expected = -8

    # Act
    result = Calculator(-5, -3).add()

    # Assert
    assert result == expected

def test_add_decimal_numbers():
    # Arrange
    a, b = 2.5, 3.7
    expected = 6.2

    # Act
    result = Calculator(a, b).add()

    # Assert
    assert abs(result - expected) < 1e-10

@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0),
    (100, 200, 300),
    (-10, 5, -5),
    (2.5, 1.5, 4.0)
])
def test_add_parameterized(a, b, expected):
    # Act
    result = Calculator(a, b).add()

    # Assert
    assert result == expected


# Test 2: Subtraction tests
def test_subtract_positive_numbers():
    # Arrange
    a, b = 10, 4
    expected = 6

    # Act
    result = Calculator(a, b).subtract()

    # Assert
    assert result == expected

def test_subtract_negative_result():
    # Arrange
    a, b = 3, 7
    expected = -4

    # Act
    result = Calculator(a, b).subtract()

    # Assert
    assert result == expected


# Test 3: Multiplication tests
def test_multiply_by_zero():
    # Arrange
    a, b = 5, 0
    expected = 0

    # Act
    result = Calculator(a, b).multiply()

    # Assert
    assert result == expected

def test_multiply_negative_numbers():
    # Arrange
    a, b = -4, -3
    expected = 12

    # Act
    result = Calculator(a, b).multiply()

    # Assert
    assert result == expected


# Test 4: Division tests
def test_divide_positive_numbers():
    # Arrange
    a, b = 10, 2
    expected = 5

    # Act
    result = Calculator(a, b).divide()

    # Assert
    assert result == expected

def test_divide_by_zero():
    # Arrange
    a, b = 10, 0

    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator(a, b).divide()

def test_divide_decimal_result():
    # Arrange
    a, b = 5, 2
    expected = 2.5

    # Act
    result = Calculator(a, b).divide()

    # Assert
    assert result == expected


# Test 5: Power function tests
def test_power_positive_exponent():
    # Arrange
    base, exponent = 2, 3
    expected = 8

    # Act
    result = Calculator(base, exponent).power()

    # Assert
    assert result == expected

def test_power_zero_exponent():
    # Arrange
    base, exponent = 5, 0
    expected = 1

    # Act
    result = Calculator(base, exponent).power()

    # Assert
    assert result == expected


# Test 7: Type validation tests
def test_add_with_string_raises_type_error():
    # Arrange
    a, b = "5", 3

    # Act & Assert
    with pytest.raises(TypeError, match="Both arguments must be numbers"):
        Calculator(a, b).add()

# def test_divide_with_none_raises_type_error():
#     """Test division with None input raises TypeError."""
#     # Arrange
#     a, b = None, 5
#
#     # Act & Assert
#     with pytest.raises(TypeError, match="Both arguments must be numbers"):
#         Calculator(a, b).divide()
