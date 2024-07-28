from unittest import TestCase
from trades.stock_trade import StockTrade
from decimal import Decimal

"""
New York Stock Exchange (NYSE)
London Stock Exchange (LSE)
Hong Kong Stock Exchange (HKEX)
"""


class TestTradeWithUnittest(TestCase):

    # Typical Testing
    # 150.50 * 100 = 15050.00
    def test_typical_stock_trade_one(self):
        trade = StockTrade("T1", "NYSE", "AAPL", Decimal("150.50"), 100, "buy")
        self.assertEqual(trade.value(), Decimal("15050.00"))
        # self.assertEqual(str(trade), "Trade ID: T1, Symbol: AAPL, Price: 150.50, Quantity: 100, Side: buy")

    # 100.75 * 10 = 1007.50
    def test_typical_fractional_price_two(self):
        trade = StockTrade("T2", "NASDAQ", "GOOGL", Decimal("100.75"), 10, "sell")
        self.assertEqual(trade.value(), Decimal("1007.50"))






