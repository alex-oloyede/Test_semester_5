import unittest
from calc import Calculator


class TestCalculatorAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Arrange
        a, b = 5, 3
        expected = 8

        # Act
        result = Calculator(a, b).add()

        # Assert
        self.assertEqual(result, expected)

    def test_add_negative_numbers(self):
        # Arrange
        a, b = -5, -3
        expected = -8

        # Act
        result = Calculator(a, b).add()

        # Assert
        self.assertEqual(result, expected)

    def test_add_decimal_numbers(self):
        # Arrange
        a, b = 2.5, 3.7
        expected = 6.2

        # Act
        result = Calculator(a, b).add()

        # Assert
        self.assertAlmostEqual(result, expected, places=7)

    def test_add_zero_values(self):
        # Arrange
        a, b = 0, 0
        expected = 0

        # Act
        result = Calculator(a, b).add()

        # Assert
        self.assertEqual(result, expected)

    def test_add_large_numbers(self):
        # Arrange
        a, b = 10 ** 6, 10 ** 6
        expected = 2 * 10 ** 6

        # Act
        result = Calculator(a, b).add()

        # Assert
        self.assertEqual(result, expected)


class TestCalculatorSubtraction(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        # Arrange
        a, b = 10, 4
        expected = 6

        # Act
        result = Calculator(a, b).subtract()

        # Assert
        self.assertEqual(result, expected)

    def test_subtract_negative_result(self):
        # Arrange
        a, b = 3, 7
        expected = -4

        # Act
        result = Calculator(a, b).subtract()

        # Assert
        self.assertEqual(result, expected)

    def test_subtract_negative_numbers(self):
        # Arrange
        a, b = -5, -3
        expected = -2

        # Act
        result = Calculator(a, b).subtract()

        # Assert
        self.assertEqual(result, expected)


class TestCalculatorMultiplication(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        # Arrange
        a, b = 5, 4
        expected = 20

        # Act
        result = Calculator(a, b).multiply()

        # Assert
        self.assertEqual(result, expected)

    def test_multiply_by_zero(self):
        # Arrange
        a, b = 5, 0
        expected = 0

        # Act
        result = Calculator(a, b).multiply()

        # Assert
        self.assertEqual(result, expected)

    def test_multiply_negative_numbers(self):
        # Arrange
        a, b = -4, -3
        expected = 12

        # Act
        result = Calculator(a, b).multiply()

        # Assert
        self.assertEqual(result, expected)

    def test_multiply_by_one(self):
        # Arrange
        a, b = 7, 1
        expected = 7

        # Act
        result = Calculator(a, b).multiply()

        # Assert
        self.assertEqual(result, expected)
