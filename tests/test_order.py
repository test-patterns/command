""" Sample problem featuring the command pattern. """

import unittest

from test_context import Order

class TestOrder(unittest.TestCase):
    """ Tests the Order class """

    def test_init(self):
        """ Tests the constructor of the Order class """
        test_order = Order("1", "Large", "Thin", "Cheese")
        self.assertEqual(test_order.quantity, "1")
        self.assertEqual(test_order.size, "Large")
        self.assertEqual(test_order.crust, "Thin")
        self.assertEqual(test_order.toppings, "Cheese")

if __name__ == '__main__':
    unittest.main()
