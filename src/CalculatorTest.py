import unittest

from Calculator import Calculator
from ParseInputFiles import ParseInputFiles
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        self.datafile = ParseInputFiles()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        filepath = './src/unitTests/Unit Test Addition.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_subtraction_method_calculator(self):
        filepath = './src/unitTests/Unit Test Subtraction.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_multiplication_method_calculator(self):
        filepath = './src/unitTests/Unit Test Multiplication.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_division_method_calculator(self):
        filepath = './src/unitTests/Unit Test Division.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
        file_data.clear()

    def test_squared_method_calculator(self):
        filepath = './src/unitTests/Unit Test Square.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
        file_data.clear()

    # def test_root_method_calculator(self):
    #     filepath = './src/unitTests/Unit Test Square Root.csv'
    #     self.assertEqual(self.calculator.root(9), 3)


if __name__ == '__main__':
    unittest.main()
