#test_stock.py
#
#Exercise 8.7

import unittest
import stock_2

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock_2.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    def test_bad_shares(self):
        s = stock_2.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '100'

if __name__ == "__main__":
    unittest.main()

