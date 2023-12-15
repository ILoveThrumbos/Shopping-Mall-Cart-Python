import unittest
from product import Product
from checkOutRegister import CheckoutRegister


class TestProduct(unittest.TestCase):
    def test_get_barcode(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_barcode(), "123")

    def test_get_desc(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_desc(), "2Litre")

    def test_get_price(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_price(), 3.5)

    def test_get_name(self):
        product = Product("123", "Milk", "2Litre", 3.5)
        self.assertEqual(product.get_name(), "Milk")


class TestCheckoutRegister(unittest.TestCase):
    def setUp(self):
        self.register = CheckoutRegister()
        self.register.products = []

    def tearDown(self):
        pass

    def test_scan_item(self):
        barcode = "123"
        p = Product(barcode, "Milk", "2Litre", 3.5)
        self.register.scan_item(barcode)
        self.assertEqual(len(self.register.products), 1)
        self.assertEqual(self.register.products[0].get_barcode(), barcode)
        self.assertEqual(self.register.products[0].get_name(), "Milk")
        self.assertAlmostEqual(self.register.products[0].get_price(), 3.5)

    def test_accept_payment(self):
        total_amount = self.register.calculate_payment_due()
        balance = self.register.accept_payment(total_amount)
        self.assertEqual(balance, 10)

    def test_init(self):
        products = []
        register = CheckoutRegister()
        self.assertEqual(register.products, products)
        self.assertEqual(register.customer_pay, 0)
        self.assertEqual(register.balance, 0)
        self.assertEqual(register.due, 0)


if __name__ == '__main__':
    unittest.main()

