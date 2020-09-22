import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(2.12, coupon.calculate_price(.99, 5, 10), 2)
        self.assertAlmostEqual(6.84, coupon.calculate_price(5.99, 5, 15), 2)
        self.assertAlmostEqual(10.18, coupon.calculate_price(9.99, 5, 20), 2)
        self.assertAlmostEqual(2.12, coupon.calculate_price(5.99, 10, 10), 2)
        self.assertAlmostEqual(1.45, coupon.calculate_price(5, 10, 15), 2)
        self.assertAlmostEqual(2.57, coupon.calculate_price(6.01, 10, 20), 2)

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(10.72, coupon.calculate_price(10, 5, 10), 2)
        self.assertAlmostEqual(21.47, coupon.calculate_price(20, 5, 15), 2)
        self.assertAlmostEqual(29.15, coupon.calculate_price(30, 5, 20), 2)
        self.assertAlmostEqual(5.95, coupon.calculate_price(10, 10, 10), 2)
        self.assertAlmostEqual(14.96, coupon.calculate_price(20, 10, 15), 2)
        self.assertAlmostEqual(24.91, coupon.calculate_price(30, 10, 20), 2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(31.8, coupon.calculate_price(30, 5, 10), 2)
        self.assertAlmostEqual(44.39, coupon.calculate_price(41, 5, 15), 2)
        self.assertAlmostEqual(50.11, coupon.calculate_price(50, 5, 20), 2)
        self.assertAlmostEqual(27.03, coupon.calculate_price(30, 10, 10), 2)
        self.assertAlmostEqual(34.98, coupon.calculate_price(40, 10, 15), 2)
        self.assertAlmostEqual(45.87, coupon.calculate_price(50, 10, 20), 2)

    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(0, coupon.calculate_price(50, 5, 10), 2)
        self.assertAlmostEqual(0, coupon.calculate_price(60, 5, 15), 2)
        self.assertAlmostEqual(0, coupon.calculate_price(70, 5, 20), 2)
        self.assertAlmostEqual(0, coupon.calculate_price(50, 10, 10), 2)
        self.assertAlmostEqual(0, coupon.calculate_price(60, 10, 15), 2)
        self.assertAlmostEqual(0, coupon.calculate_price(70, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
