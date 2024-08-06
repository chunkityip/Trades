import unittest
from decimal import Decimal
from trades.stock import Stock

class TestTradeWithUnittest(unittest.TestCase):

    # Typical Testing: two different companies

    # Test the price should be 150.50 * 100 = 15050.00
    def test_typical_stock_trade_one(self):
        trade = Stock("T1", "NYSE", "AAPL", Decimal("150.50"), 100, "buy")
        self.assertEqual(trade.value(), Decimal("15050.00"))
        expected_str = "Trade ID: T1, Symbol: AAPL, Price: 150.50, Quantity: 100, Side: buy"
        self.assertEqual(str(trade), expected_str)

    # Test the price should be 100.75 * 10 = 1007.50
    def test_typical_fractional_price_two(self):
        trade = Stock("T2", "NASDAQ", "GOOGL", Decimal("100.75"), 10, "sell")
        self.assertEqual(trade.value(), Decimal("1007.50"))

    # Boundary Testing: small and large quantity, minimum and maximum price

    # Test with quantity 1
    # 1.0 * 1 = 1
    def test_small_quantity(self):
        trade = Stock("T3", "NYSE", "VOO", Decimal("1.00"), 1, "buy")
        self.assertEqual(trade.value(), Decimal("1.00"))

    # Test with quantity 1000000
    # 1000000 * 5 = 5000000.00
    def test_large_quantity(self):
        trade = Stock("T4", "NYSE", "VOO", Decimal("5.00"), 1000000, "buy")
        self.assertEqual(trade.value(), Decimal("5000000.00"))

    # Test with the minimum price
    # 0.01 * 100 = 1.00
    def test_minimum_price(self):
        trade = Stock("T5", "NYSE", "VOO", Decimal("0.01"), 100, "sell")
        self.assertEqual(trade.value(), Decimal("1.00"))

    # Test with the maximum price
    # 999999.99 * 1 = 999999.99
    def test_maximum_price(self):
        trade = Stock("T6", "NYSE", "VOO", Decimal("999999.99"), 1, "sell")
        self.assertEqual(trade.value(), Decimal("999999.99"))

    # Erroneous Testing
    def test_invalid_trade_id(self):
        with self.assertRaises(ValueError):
            Stock("", "NYSE", "AAPL", Decimal("100.00"), 10, "buy")

    def test_invalid_exchange(self):
        with self.assertRaises(ValueError):
            Stock("T7", "INVALID", "AAPL", Decimal("100.00"), 10, "buy")

    def test_invalid_symbol(self):
        with self.assertRaises(ValueError):
            Stock("T8", "NYSE", "", Decimal("100.00"), 10, "buy")

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            Stock("T9", "NYSE", "AAPL", Decimal("-100.00"), 10, "buy")

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            Stock("T10", "NYSE", "AAPL", Decimal("0.00"), 10, "buy")

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            Stock("T11", "NYSE", "AAPL", Decimal("100.00"), -10, "buy")

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            Stock("T12", "NYSE", "AAPL", Decimal("100.00"), 0, "buy")

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            Stock("T13", "NYSE", "AAPL", Decimal("100.00"), 10, "hold")

if __name__ == "__main__":
    unittest.main()

