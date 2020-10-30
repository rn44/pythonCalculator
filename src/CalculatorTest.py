import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        filepath = './unitTests/Unit Test Addition.csv'
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_subtraction_method_calculator(self):
        filepath = './unitTests/Unit Test Subtraction.csv'
        self.assertEqual(self.calculator.subtract(2, 2), 0)

    def test_multiplication_method_calculator(self):
        filepath = './unitTests/Unit Test Multiplication.csv'
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_division_method_calculator(self):
        filepath = './unitTests/Unit Test Division.csv'
        self.assertEqual(self.calculator.divide(6, 3), 2)

    def test_squared_method_calculator(self):
        filepath = './unitTests/Unit Test Square.csv'
        self.assertEqual(self.calculator.square(3), 9)

    def test_root_method_calculator(self):
        filepath = './unitTests/Unit Test Square Root.csv'
        self.assertEqual(self.calculator.root(9), 3)


if __name__ == '__main__':
    unittest.main()
