from decimal import Decimal
from unittest import TestCase
from trades.stock_trade import StockTrade

class TestTrade(TestCase):
    def test_stock_trade_value(self):
        trade = StockTrade("id1", "NYSE", "AAPL", Decimal("150.50"), 100, "buy")
        self.assertNotEqual(trade.value(), Decimal("1.00"))
        self.assertEqual(trade.symbol , "AAPL")

