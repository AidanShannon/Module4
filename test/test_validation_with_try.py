import unittest
from input_validation import validation_with_try


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, -89, 78)


if __name__ == '__main__':
    unittest.main()
