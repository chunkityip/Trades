from unittest import TestCase
from trades.stock_trade import StockTrade
from decimal import Decimal

"""
New York Stock Exchange (NYSE)
London Stock Exchange (LSE)
Hong Kong Stock Exchange (HKEX)
"""


class TestTradeWithUnittest(TestCase):

    # Typical Testing : two different companies

    # Test the price should be 150.50 * 100 = 15050.00
    def test_typical_stock_trade_one(self):
        trade = StockTrade("T1", "NYSE", "AAPL", Decimal("150.50"), 100, "buy")
        self.assertEqual(trade.value(), Decimal("15050.00"))
        self.assertEqual(str(trade), "Trade ID: T1, Symbol: AAPL, Price: 150.50, Quantity: 100, Side: buy")

    # Test the price should be 100.75 * 10 = 1007.50
    def test_typical_fractional_price_two(self):
        trade = StockTrade("T2", "NASDAQ", "GOOGL", Decimal("100.75"), 10, "sell")
        self.assertEqual(trade.value(), Decimal("1007.50"))

    # Boundary Testing : small and large quantity , minimum and maximum price

    # Test with quantity 1
    # 1.0 * 1 = 1
    def test_small_quantity(self):
        trade = StockTrade("T3", "NYSE", "VO0", Decimal("1.00"), 1, "buy")
        self.assertEqual(trade.value(), Decimal("1.00"))

    # Test with quantity 1000000
    # 1000000, * 5 = 5000000.00
    def test_large_quantity(self):
        trade = StockTrade("T3", "NYSE", "VO0", Decimal("5.00"), 1000000, "buy")
        self.assertEqual(trade.value(), Decimal("5000000.00"))

    # Test with the minimum price
    # 0.01 * 100 = 1.00
    def test_minimum_price(self):
        trade = StockTrade("T3", "NYSE", "VO0", Decimal("0.01"), 100, "sell")
        self.assertEqual(trade.value(), Decimal("1.00"))

    # Test with the maximum price

    def test_maximum_price(self):
        trade = StockTrade("T3", "NYSE", "VO0", Decimal("999999.99"), 1, "sell")
        self.assertEqual(trade.value(), Decimal("999999.99"))

    # Erroneous Testing
    def test_invalid_trade_id(self):
        with self.assertRaises(ValueError):
            StockTrade("", "NYSE", "AAPL", Decimal("100.00"), 10, "buy")