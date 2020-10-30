import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)

    def test_subtraction_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)

    def test_multiplication_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 3), 6)

    def test_division_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 3), 2)

    def test_squared_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(3), 9)

    def test_root_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.root(9), 3)


if __name__ == '__main__':
    unittest.main()
